@echo off

cd ..

py ocr.py /img/dnd.png -l eng
echo eng test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    ECHO OK
)
pause
echo 
py ocr.py /img/dnd.png -l ita
echo ita test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    ECHO OK
)
pause
echo
py ocr.py /img/dnd.png -l fra
echo fra test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO OK
) else (
    ECHO FAILED
)
cd test_case
: END