*If The VENV file was added to the github the do this*
- git rm -r --cached venv
- git commit -m "Remove venv from the repository"

<hr>

SETUP HELP - https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3

<h1>Step 1 — Installing Flask</h1>

Create a project folder and a .venv folder within:
- python3 -m venv .venv

Before you work on your project, activate the corresponding environment:
- . .venv/bin/activate

Within the activated environment, use the following command to install Flask:
- pip install Flask

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
