@echo off
setlocal
cd /d %~dp0
start "" "C:\Users\%USERNAME%\AppData\Local\Chromium\Application\chrome.exe" --user-data-dir="%~dp0User Data"
endlocal