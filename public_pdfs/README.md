# public_pdfs

下部帯を隠した、お客様共有用PDFの出力先です。

ここに出力されたPDFだけを提案ページに掲載します。

PDFは0枚、1枚、複数枚のどの状態でも運用できます。
複数掲載する場合は、`index.html` の「共有PDF資料」欄にPDFごとのタイトル、コメント、「PDFを見る」ボタンを追加します。

リンク先は必ず以下のような相対パスにしてください。

```html
<a class="pdf-button" href="./public_pdfs/物件資料_お客様共有用.pdf" target="_blank" rel="noopener">PDFを見る</a>
```

公開前に必ず加工後PDFを目視確認してください。
