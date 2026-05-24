# 複数PDF掲載手順

加工済みPDFを提案ページへ複数掲載するための手順です。

## 基本方針

- 元PDFは `originals/` に置く
- `originals/` のPDFはGit管理しない
- 元PDFをGitHub Pages上に直接公開しない
- `tools/mask_pdf_bottom.bat` で加工済みPDFを `public_pdfs/` に出力する
- `index.html` に掲載するPDFは `public_pdfs/` のPDFだけにする
- PDFは0枚、1枚、複数枚のどれでも成立する

## index.html の掲載例

PDFを1件追加する場合は、`共有PDF資料` セクション内に以下を追加します。

```html
<article class="pdf-card">
  <div>
    <h3>物件資料タイトル</h3>
    <p>お客様に伝えたい補足コメントを入れます。</p>
  </div>
  <a class="pdf-button" href="./public_pdfs/加工済みPDF名.pdf" target="_blank" rel="noopener">PDFを見る</a>
</article>
```

複数PDFを載せる場合は、この `article` をPDFの数だけ並べます。
PDFが0枚の場合は、空状態の文言だけを表示します。

## 公開前チェックリスト

- [ ] 元PDFが `originals/` に保存されている
- [ ] 元PDFを `assets/` や `public_pdfs/` に直接置いていない
- [ ] `tools/mask_pdf_bottom.bat` を実行した
- [ ] 加工済みPDFが `public_pdfs/` に出力されている
- [ ] `review_previews/` で加工前後のPNGを確認した
- [ ] 加工済みPDFを開いて、下部帯に隠したい情報が残っていないことを確認した
- [ ] `index.html` のPDFリンクがすべて `./public_pdfs/...` になっている
- [ ] PDFごとにタイトルとコメントが入っている
- [ ] `PDFを見る` ボタンが表示されている
- [ ] ローカルでページ表示とPDFリンクを確認した

## 注意

REINS由来で外部共有不可の情報、広告不可物件の詳細資料、個人情報、管理会社の内部情報は掲載しないでください。
