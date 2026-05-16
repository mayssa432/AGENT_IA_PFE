@echo off
chcp 65001
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
python -X utf8 main.py %*
