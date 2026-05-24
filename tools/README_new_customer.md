# 別のお客様用ページ作成手順

## 方針

お客様ごとにGitHubリポジトリを分けます。

例：

```text
katsukawa-proposal
tanaka-proposal
suzuki-proposal
```

URL例：

```text
https://gogo55st-bit.github.io/tanaka-proposal/
```

## 手順

1. GitHubで新しいリポジトリを作成する
   - 例：`tanaka-proposal`
   - Publicで作成する

2. `katsukawa-proposal` を参考に初期構成を作る
   - `index.html`
   - `README.md`
   - `tools/push_update.bat`
   - 必要に応じて `assets/`

3. お客様名、タイトル、提案内容、必要ファイルを差し替える

4. 画像やPDFは必要な場合だけ追加する
   - エリアMAPは必須ではない
   - 物件PDFは必須ではない
   - テキスト提案のみでも成立させる

5. GitHub Pagesを有効化する
   - Source：`main`
   - Folder：`/root`

6. 正式URLを確認する

```text
https://gogo55st-bit.github.io/リポジトリ名/
```

7. `tools/push_update.bat` のパスとURLを新顧客用に変更する

8. `README.md` を新顧客名に合わせて変更する

## 新顧客用 `push_update.bat` で変更する箇所

```bat
cd /d "C:\Users\user\Documents\GO_AI_COMPANY_OBSIDIAN\01_Projects\物件GO\GitHubPages\新リポジトリ名"
```

表示するURL：

```text
https://gogo55st-bit.github.io/新リポジトリ名/
```

## 注意事項

- 既存の勝川さんページを別顧客用に直接上書きしない
- REINS由来で外部共有不可の資料は公開しない
- ページ公開前にスマホ表示を確認する
- URLをお客様に送る前に、必ずGitHub Pagesで200応答を確認する
