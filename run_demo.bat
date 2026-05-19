@echo off
chcp 65001 >nul
SET PYTHONUTF8=1
SET PYTHONPATH=%~dp0

echo.
echo ================================================================
echo   Agent IA Appium — Démo PFE
echo ================================================================
echo.

:: Vérifier l'environnement virtuel
IF NOT EXIST "%~dp0venv\Scripts\python.exe" (
    echo Environnement virtuel introuvable -- creez-le d'abord :
    echo   python -m venv venv
    echo   venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

SET PYTHON=%~dp0venv\Scripts\python.exe

IF "%1"=="server" (
    echo Lancement du serveur web (http://localhost:5000^) ...
    "%PYTHON%" chat_server.py
) ELSE IF "%1"=="tests" (
    echo Test unitaires ...
    "%~dp0venv\Scripts\pytest" tests/ --ignore=tests/test_agent.py --ignore=tests/test_groq_client.py -q
) ELSE IF "%1"=="livrable" (
    echo Demo livrable #%2 ...
    "%PYTHON%" demo_soutenance.py --livrable %2
) ELSE (
    echo Demo complete (tous les livrables) ...
    "%PYTHON%" demo_soutenance.py
)

echo.
echo Termine. Appuyez sur une touche...
pause >nul
