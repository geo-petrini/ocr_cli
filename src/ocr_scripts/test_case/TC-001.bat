@echo off

cd ..

py ocr.py /img/dnd.png
echo png test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    ECHO OK
)
pause
echo 
py ocr.py ../img/itatxtjpg.jpg 
echo jpg test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    ECHO OK
)
pause
echo
py ocr.py ../img/engtextpng.jpeg
echo jpeg test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    ECHO OK
)
pause
echo
py ocr.py ../img/error.tiff
echo tiff test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO OK
) else (
    ECHO FAILED
)
cd test_case
: END