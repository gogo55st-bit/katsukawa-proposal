@echo off
REM 新しいお客様用リポジトリへコピーしたら、下のパスとURLを変更してください。
cd /d "C:\Users\user\Documents\GO_AI_COMPANY_OBSIDIAN\01_Projects\物件GO\GitHubPages\REPOSITORY_NAME"
set PATH=%ProgramFiles%\Git\cmd;%ProgramFiles%\GitHub CLI;%PATH%
git status
git add .
git commit -m "update proposal page"
git push origin main
echo.
echo 公開URL:
echo https://gogo55st-bit.github.io/REPOSITORY_NAME/
echo.
pause
