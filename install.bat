@echo off
title Remote Relay - Installation
echo Installation des dependances...
py -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERREUR : Python/pip n'est pas disponible.
    pause
    exit /b 1
)
echo.
echo Installation terminee.
pause
