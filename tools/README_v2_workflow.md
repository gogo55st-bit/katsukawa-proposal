# 勝川さん v2 提案ページ更新手順

正式URLは常に以下です。

```text
https://gogo55st-bit.github.io/katsukawa-proposal/
```

## 前提

現在の公開済みv1は `archive/v1/` に保管済みです。
v2を作るときも、公開URLは変えず、リポジトリ直下の `index.html` を更新します。

## 手順

1. v2で何を提案するか決める
2. 必要に応じて画像、PDF、コメントを用意する
3. エリアMAPは必要な場合だけ作成する
4. 物件PDFを掲載する場合は、元PDFを `originals/` に入れる
5. `tools/mask_pdf_bottom.bat` を実行し、下部帯を隠したPDFを作成する
6. `review_previews/` と加工済みPDFを開き、隠したい情報が残っていないか必ず確認する
7. 複数PDFを掲載する場合は、`tools/README_multiple_pdfs.md` の形で `index.html` に追加する
8. 新しい `index.html` や必要ファイルをルートに配置する
9. ローカルで表示確認する
10. `tools/push_update.bat` を実行する
11. 正式URLで反映確認する
12. LINE送信用文面を作る

## PDF掲載時の注意

元PDFは `originals/` に保存します。
`originals/` はGit管理しないため、GitHub Pagesには公開しません。

お客様共有用には、必ず加工済みPDFだけを使ってください。
加工済みPDFは `public_pdfs/` に保存します。
提案ページからリンクする場合も、必ず `./public_pdfs/...` を使ってください。

公開前に必ず加工後PDFを確認してください。

## LINE文面の考え方

```text
勝川さん

追加の物件提案ページを更新しました。
以下よりご確認ください。

https://gogo55st-bit.github.io/katsukawa-proposal/
```
