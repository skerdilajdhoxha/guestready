# Installation
- Please clone the test project from [Github repo](https://github.com/skerdilajdhoxha/guestready).
- Create a virtual environment: `python3 -m venv venv` and then activate it `source venv/bin/activate`.
- Install dependencies: `pip install -r requirements.txt`
- Cd into src and run migrations `python manage.py migrate`
- Run tests: `python manage.py test`

# Important
- This app must use PostgreSQL because of `distinct('field')` 
