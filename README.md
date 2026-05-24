# Katsukawa Proposal Page

勝川さん専用の不動産提案ページです。

正式な共有URL:

```text
https://gogo55st-bit.github.io/katsukawa-proposal/
```

## 重要な方針

このリポジトリは勝川さん専用ページとして運用します。
`/katsukawa/`、`/sato/`、`/tanaka/` のような顧客別フォルダ構成には戻しません。
公開ページはリポジトリ直下の `index.html` を正とします。

## ローカル管理場所

```text
C:\Users\user\Documents\GO_AI_COMPANY_OBSIDIAN\01_Projects\物件GO\GitHubPages\katsukawa-proposal
```

## 通常の更新手順

1. `index.html`、`styles.css`、画像、加工済みPDFを必要に応じて差し替える
2. ローカルでページを開いて内容確認する
3. `tools\push_update.bat` を実行する
4. 数分後、正式URLで反映を確認する

正式URL:

```text
https://gogo55st-bit.github.io/katsukawa-proposal/
```

## v2や別顧客ページの考え方

勝川さんv2を作る場合は、まず `tools/README_v2_workflow.md` を確認してください。
別のお客様用ページを作る場合は、`tools/README_new_customer.md` を確認してください。
お客様ごとにリポジトリを分ける方針です。

```text
katsukawa-proposal
tanaka-proposal
suzuki-proposal
```

エリアMAP、物件PDF、物件画像、補足資料はすべて任意です。
案件によって、画像なし、PDFなし、テキスト提案のみでも進められるようにします。

## PDF下部帯のマスク運用

お客様共有用PDFを作る場合は、元PDFをそのまま公開せず、下部帯を隠した加工済みPDFだけを掲載します。

### フォルダ

```text
originals/
  元PDFを置く場所。Git管理しない。GitHub Pagesに公開しない。

public_pdfs/
  下部帯を隠した、お客様共有用PDFの出力先。

assets/pdfs/
  元PDFを置かない。現在の運用ではPDF掲載に使わない。

review_previews/
  加工前後の確認用PNG。Git管理しない。GitHub Pagesに公開しない。
```

### 手順

1. 元PDFを `originals/` に入れる
2. `tools/mask_pdf_bottom.bat` を実行する
3. `public_pdfs/` に加工済みPDFが生成される
4. `review_previews/` で加工前後のPNGを確認する
5. 加工済みPDFを開き、下部に隠したい情報が残っていないか必ず目視確認する
6. 問題なければ提案ページに掲載し、`tools/push_update.bat` で公開する

### 複数PDF掲載

複数の加工済みPDFを掲載する場合は、`tools/README_multiple_pdfs.md` を確認してください。
`index.html` の「共有PDF資料」欄に、PDFごとのタイトル、コメント、「PDFを見る」ボタンを追加します。
PDFが0枚、1枚、複数枚のどの状態でも成立します。

公開ページに掲載するPDFリンクは必ず `./public_pdfs/...` にしてください。
元PDFや `originals/` 内のファイルへ直接リンクしないでください。

### 公開前チェックリスト

- [ ] 元PDFは `originals/` に保存している
- [ ] 元PDFをGit管理していない
- [ ] `tools/mask_pdf_bottom.bat` で加工済みPDFを作成した
- [ ] `review_previews/` で加工前後を確認した
- [ ] `public_pdfs/` の加工済みPDFを開いて目視確認した
- [ ] 下部帯に隠したい情報が残っていない
- [ ] `index.html` のPDFリンクが `./public_pdfs/...` だけになっている
- [ ] PDFごとにタイトルとコメントを付けている

### 重要

公開前に必ず加工後PDFを確認してください。
元PDFをGitHub Pages上に公開しないでください。

`tools/mask_pdf_bottom.py` はPDFを一度画像化し、各ページ下部を白塗りしてから再PDF化します。
これにより、PDF内部に隠したい下部情報が残るリスクを下げます。

## 掲載しない情報

GitHub Pagesで公開したページはインターネット上で見られる状態になります。
以下は掲載しないでください。

```text
・個人情報
・申込書類
・身分証
・オーナー情報
・管理会社の内部情報
・REINS由来で外部共有不可の情報
・広告不可物件の詳細資料
```

お客様共有用として問題ない内容だけを掲載してください。
