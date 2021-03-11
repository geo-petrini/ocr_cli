@echo off

py prova.py ../itatxtpng.png -d 

IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    echo OK
)

