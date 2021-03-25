@echo off

py ocr.py ../img/itatxtpng.png
echo png test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    echo OK
)
pause
echo 
py ocr.py ../img/itatxtjpg.jpg 
echo jpg test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO FAILED
) else (
    echo OK
)
pause
echo
py ocr.py ../img/engtextpng.jpeg
echo jpeg test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO OK
) else (
    echo FAILED
)
pause
echo
py ocr.py ../img/error.tiff
echo tiff test:
IF /I "%ERRORLEVEL%" NEQ "0" (
    ECHO OK
) else (
    echo FAILED
)

pause