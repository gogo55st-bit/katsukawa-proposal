@echo off
cd /d "%~dp0.."

set PYTHON_EXE=C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
if not exist "%PYTHON_EXE%" set PYTHON_EXE=python

"%PYTHON_EXE%" -c "import pypdfium2, PIL" 2>nul
if errorlevel 1 (
  echo Installing PDF mask dependencies...
  "%PYTHON_EXE%" -m pip install -r tools\requirements_pdf_mask.txt
)

"%PYTHON_EXE%" tools\mask_pdf_bottom.py

echo.
echo 加工後PDFは public_pdfs に出力されます。
echo review_previews で加工前後のPNGを確認してください。
echo 公開前に、必ず加工後PDFを目視確認してください。
pause
