*If The VENV file was added to the github the do this*
- git rm -r --cached venv
- git commit -m "Remove venv from the repository"

<hr>

Create a project folder and a .venv folder within:
- python3 -m venv .venv

Before you work on your project, activate the corresponding environment:
- . .venv/bin/activate

Within the activated environment, use the following command to install Flask:
- pip install Flask
