# 別のお客様用ページ作成手順

別のお客様が来たときは、お客様ごとにGitHubリポジトリを分けます。

```text
katsukawa-proposal
tanaka-proposal
suzuki-proposal
```

## 手順

1. GitHubで新しいリポジトリを作成する
2. `template/` を参考に初期構成を作る
3. お客様名、タイトル、提案内容、必要ファイルを差し替える
4. 画像やPDFは必要な場合だけ追加する
5. エリアMAPは必須にしない
6. 物件PDFを掲載する場合は、元PDFを直接公開せず、加工済みPDFだけを使う
7. GitHub Pagesを有効化する
8. 正式URLを確認する
9. `tools/push_update.bat` のパスとURLを新顧客用に変更する
10. READMEを新顧客名に合わせて変更する

URL例:

```text
https://gogo55st-bit.github.io/tanaka-proposal/
```

## PDF掲載時の注意

元PDFは `originals/` に保存し、Git管理しないようにします。
お客様共有用PDFは、下部帯など隠したい情報を加工したうえで `public_pdfs/` または `assets/pdfs/` に保存します。

公開前に必ず加工後PDFを確認してください。
REINS由来で外部共有不可の情報や、広告不可物件の詳細資料は掲載しないでください。

## 任意資料の考え方

エリアMAP、物件PDF、画像資料、補足資料はすべて任意です。
テキスト提案だけでも成立する構成にしてください。
