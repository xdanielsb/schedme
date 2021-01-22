# Schedme

An application who reconnect us with our hobbies or at least for that it was designed.

to see the application running click on the following link [DEMO](https://www.youtube.com/watch?v=dQw4w9WgXcQ)).

after looking that DEMO you can see the deployment on scalingo here [deployment on scalingo](https://schedme.osc-fr1.scalingo.io/)

## Local installation

Clone the repo in the folder schedme/ run the following commands

```sh
 $ python3 -m venv env-django
 $ source env-django/bin/activate
 (env-django)$ pip3 install -r requirements.txt
 (env-django)$ cd app/
 (env-django)$ python manage.py runserver
```

## Google Authentication

In order to use Google API services when the app is installed, you need to create a [Google API project](https://console.developers.google.com/apis/dashboard?project=schedme-302307&folder=&organizationId=).

Then, on the Google developers console :

- Libraries :Add the Google Calendar Library
- Setup the OAuth Authorization Screen
  - Add the following access level
    - .../auth/userinfo.email
    - .../auth/userinfo.profile
    - .../auth/calendar.events.freebusy
    - .../auth/calendar.events.owned
  - Add test users
- Credentials : create an ID client OAuth 2.0
  - Add your website in the javascript origins (both `http://localhost:8000` and `http://localhost:8080` if you're running on local)
  - In the redirection origins
    - add `yourwebsite/accounts/google/login/callback/` (`http://localhost:8000/accounts/google/login/callback/` if running local)
    - add `yourwebsite/students/callback` (`http://localhost:8080` if running local)
  - Download the JSON file associated, and keep client ID and secret code

If you're running the programm locally, put the JSON file in the root folder of the project.

If you're running the programm on server, set the value of the CLIENT_CONFIG environment variable as the content of the JSON file.

Once the project is running, add Google as a django social app :

- connect to `yourwebsite/admin` with a superuser account (if you don't have created one, you can use username:admin - password:admin)
- change the password of the admin user
- create a social application
  - Provider: Google
  - name: Google API
  - Client ID: copy the OAuth 2.0 client ID from earlier
  - Secret key: copy the OAuth secret key from earlier
  - Sites: add example.com

## Deploy on Scalingo

Be sure you have a Scalingo account with ssh keys properly set.

Create a scalingo project. Get your project url.

Add environments variables:

- ALLOWED_HOSTS=yourprojecturl
- CLIENT_CONFIG=*JSON token from previous part*

Follow the instructions on the **code** section.

Then you can access your project on its url. Don't forget to set the admin account, as described in previous section.
