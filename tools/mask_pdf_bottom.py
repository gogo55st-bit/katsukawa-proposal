from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, JpegImagePlugin  # noqa: F401
except ImportError as exc:
    raise SystemExit("Pillow is required. Run: python -m pip install -r tools/requirements_pdf_mask.txt") from exc

try:
    import pypdfium2 as pdfium
except ImportError as exc:
    raise SystemExit("pypdfium2 is required. Run: python -m pip install -r tools/requirements_pdf_mask.txt") from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
ORIGINALS_DIR = REPO_ROOT / "originals"
PUBLIC_PDFS_DIR = REPO_ROOT / "public_pdfs"
ASSETS_PDFS_DIR = REPO_ROOT / "assets" / "pdfs"
PREVIEW_DIR = REPO_ROOT / "review_previews"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rasterize PDFs, white-mask the bottom band of each page, and rebuild customer-share PDFs."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=None,
        help="Input PDF. If omitted, all PDFs in originals/ are processed.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PUBLIC_PDFS_DIR,
        help="Directory for customer-share PDFs. Default: public_pdfs/",
    )
    parser.add_argument(
        "--mask-ratio",
        type=float,
        default=0.13,
        help="Bottom page height ratio to white-mask. Default: 0.13.",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=2.0,
        help="Render scale. Higher is sharper and larger. Default: 2.0.",
    )
    parser.add_argument(
        "--also-copy-to-assets",
        action="store_true",
        help="Also copy generated PDFs to assets/pdfs/ for existing pages that link there.",
    )
    return parser.parse_args()


def safe_output_name(pdf_path: Path) -> str:
    return f"{pdf_path.stem}_お客様共有用.pdf"


def render_page_to_image(page: pdfium.PdfPage, scale: float) -> Image.Image:
    bitmap = page.render(scale=scale)
    return bitmap.to_pil().convert("RGB")


def mask_bottom(image: Image.Image, mask_ratio: float) -> Image.Image:
    output = image.copy()
    mask_height = max(1, int(output.height * mask_ratio))
    y0 = output.height - mask_height
    draw = ImageDraw.Draw(output)
    draw.rectangle([(0, y0), (output.width, output.height)], fill="white")
    return output


def process_pdf(pdf_path: Path, output_dir: Path, mask_ratio: float, scale: float) -> Path:
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    output_dir.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    preview_subdir = PREVIEW_DIR / pdf_path.stem
    preview_subdir.mkdir(parents=True, exist_ok=True)

    document = pdfium.PdfDocument(str(pdf_path))
    masked_images: list[Image.Image] = []

    for page_index in range(len(document)):
        page = document[page_index]
        before = render_page_to_image(page, scale)
        after = mask_bottom(before, mask_ratio)

        before.save(preview_subdir / f"page_{page_index + 1:03d}_before.png")
        after.save(preview_subdir / f"page_{page_index + 1:03d}_after.png")
        masked_images.append(after)

    if not masked_images:
        raise ValueError(f"No pages found: {pdf_path}")

    output_path = output_dir / safe_output_name(pdf_path)
    first, *rest = masked_images
    first.save(output_path, save_all=True, append_images=rest)
    return output_path


def list_inputs(input_pdf: Path | None) -> list[Path]:
    if input_pdf:
        return [input_pdf]
    if not ORIGINALS_DIR.exists():
        return []
    return sorted(ORIGINALS_DIR.glob("*.pdf")) + sorted(ORIGINALS_DIR.glob("*.PDF"))


def main() -> int:
    args = parse_args()
    inputs = list_inputs(args.input)

    if not inputs:
        print("No input PDFs found.")
        print(f"Place source PDFs in: {ORIGINALS_DIR}")
        return 1

    generated: list[Path] = []
    for pdf_path in inputs:
        print(f"Processing: {pdf_path}")
        output_path = process_pdf(pdf_path, args.output_dir, args.mask_ratio, args.scale)
        generated.append(output_path)
        print(f"Generated: {output_path}")

        if args.also_copy_to_assets:
            ASSETS_PDFS_DIR.mkdir(parents=True, exist_ok=True)
            asset_path = ASSETS_PDFS_DIR / output_path.name
            shutil.copy2(output_path, asset_path)
            print(f"Copied to: {asset_path}")

    print("\nReview before/after PNGs here:")
    print(PREVIEW_DIR)
    print("\nIMPORTANT: Open and visually inspect every generated PDF before publishing.")
    for output_path in generated:
        print(f"- {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
