@echo off
REM -- pensare ad una variante col proxy
REM -- pensare a pip.ini con le impostazioni proxy

REM -- Installa i moduli necessari dal file di testo dei requisiti --
py -m pip install -r requirements.txt
if %errorlevel% == 0  echo Dipendenze installate, ora puoi usare l'ocr
pause