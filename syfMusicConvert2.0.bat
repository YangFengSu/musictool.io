chcp 65001

@echo off
setlocal enabledelayedexpansion

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "year=!dt:~0,4!"
set "month=!dt:~4,2!"
set "day=!dt:~6,2!"

set output_folder=%YEAR%_%MONTH%_%DAY%
if not exist "!output_folder!" mkdir "!output_folder!"

for %%I in (*.m4a) do (
    set "output_file=!output_folder!\%%~nI.mp3"
    ffmpeg -i "%%I" -acodec libmp3lame -q:a 0 "!output_file!"
)

for %%I in (*.flac *.mp4) do (
    set "output_file=!output_folder!\%%~nI.mp3"
    ffmpeg -i "%%I" -q:a 0 -map a "!output_file!"
)

endlocal
