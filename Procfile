web: gunicorn app.wsgi --chdir ./app --log-file -
postdeploy: python ./manage.py createsuperuser --no-input