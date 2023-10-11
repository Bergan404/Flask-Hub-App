*If The VENV file was added to the github the do this*
- git rm -r --cached venv
- git commit -m "Remove venv from the repository"

<hr>

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

`from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>`
