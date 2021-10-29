# CMPUT404-F21-Project

This is a blogging/social network platform that will allow the importing of other sources of posts (github, twitter, etc.) as well allow the distributing sharing of posts and content. This project is initially made for CMPUT404 Fall 2021 at University of Alberta.

## Local Deployment
### Prerequisite
- Python 3.6+
- Django
- (Recommended) Python virtual environment

### Instructions
1. `git clone` this repository
2. `cd CMPUT404-F21-Project\backend` to navigate to the app folder
3. `python3 manage.py makemigrations`
4. `python3 manage.py migrate`
5. `python3 manage.py createsuperuser` to create an admin account. Fill the information for signing up.
6. `python3 manage.py runserver`. After this, you should be able to access the app on your local host.

## Documentation
Internal documentation is inside /docs folder. You can `cd docs` or visit the links below.
- [References](https://github.com/GraceFu/CMPUT404-F21-Project/blob/main/docs/references.md)
