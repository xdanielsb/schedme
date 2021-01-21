web: gunicorn app.wsgi --chdir ./app --log-file -
postdeploy: python ./app/manage.py createsuperuser --no-input