rem step 1: create virtual env
python -m venv .venv

rem step 2: activate the virtual env
.venv\Scripts\activate.bat

rem step 3: install dependencies
pip install -r .venv\requirements.txt

rem step 4: setup database
python api\manage.py makemigrations
python api\manage.py migrate

rem step 5: create super user
python api\manage.py createsuperuser --email admin@example.com --username admin

rem step 6: load test data into db