@echo off
cd /d "C:\Users\user\Documents\GO_AI_COMPANY_OBSIDIAN\01_Projects\物件GO\GitHubPages\katsukawa-proposal"
set PATH=%ProgramFiles%\Git\cmd;%ProgramFiles%\GitHub CLI;%PATH%
git status
git add .
git commit -m "update proposal page"
git push origin main
echo.
echo 公開URL:
echo https://gogo55st-bit.github.io/katsukawa-proposal/
echo.
echo LINE送信用:
echo 勝川さん
echo.
echo 都筑区勤務を前提に、車通勤しやすい候補エリアと物件情報をまとめました。
echo まずはこちらのページをご確認ください。
echo.
echo https://gogo55st-bit.github.io/katsukawa-proposal/
echo.
pause
