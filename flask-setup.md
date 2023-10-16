*If The VENV file was added to the github the do this*
- git rm -r --cached venv
- git commit -m "Remove venv from the repository"

<hr>

SETUP HELP - https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3

<h1>Step 1 — Installing Flask</h1>

Create a project folder and a .venv folder within:
- python3 -m venv .venv
- virtualenv env

Before you work on your project, activate the corresponding environment:
- . .venv/bin/activate
- source env/bin/activate

Within the activated environment, use the following command to install Flask:
- pip install Flask
- pip install flask-sqlalchemy

<h1>Step 2 — Creating a Simple Application</h1>

In your flask_app directory, open a file named app.py for editing
- touch app.py

Write the following code inside the app.py file to get started:

```
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>
```

<h1>Step 3 — Running the Application</h1>

while in your flask_app directory with your virtual environment activated, tell Flask where to find the application (app.py in your case) using the FLASK_APP environment variable with the following command (on Windows, use set instead of export):
- export FLASK_APP=app

Then specify that you want to run the application in development mode (so you can use the debugger to catch errors) with the FLASK_VENV environment variable:
- export FLASK_VENV=development

Lastly, run the application using the flask run command:
- flask run
- python3 app.py


<h1>Step 4 — Routes and View Functions</h1>

To add routes to the application inside the **app.py file** you can add this, this would be added under the (/) route:

```
@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'
```

To add a template for the page we need to call *render_template* also create a templates folder to hold all the files:

```
from flask import Flask, render_template

@app.route('/about/')
def about():
    return render_template('about.html')
```

```
├── templates
        └── <each-template>.html
```

SCSS
 pip install Flask Flask-Assets libsass
