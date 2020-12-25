@echo off
rem step 1: create virtual env
python -m venv .venv

rem step 2: activate the virtual env
call .venv\Scripts\activate.bat

rem step 3: install dependencies
pip install -r .venv\requirements.txt

rem step 4: setup database
rem python api\manage.py makemigrations
rem python api\manage.py migrate

@echo on
cmd /k