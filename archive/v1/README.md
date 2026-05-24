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

## 現在の構成

```text
katsukawa-proposal/
├─ index.html
├─ styles.css
├─ assets/
│  ├─ area-map.svg
│  └─ pdfs/
└─ tools/
   └─ push_update.bat
```

## バックアップ

公開済みページのローカルバックアップ:

```text
C:\Users\user\Documents\GO_AI_COMPANY_OBSIDIAN\01_Projects\物件GO\GitHubPages_Backups\katsukawa-proposal_2026-05-24_published
```

## 通常の更新手順

1. `index.html`、`styles.css`、`assets/` 内の画像やPDFを必要に応じて差し替える
2. ローカルでページを開いて内容確認する
3. `tools\push_update.bat` を実行する
4. 数分後、正式URLで反映を確認する

正式URL:

```text
https://gogo55st-bit.github.io/katsukawa-proposal/
```

## 手動でpushする場合

```bash
git status
git add .
git commit -m "update proposal page"
git push origin main
```

## 注意事項

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
