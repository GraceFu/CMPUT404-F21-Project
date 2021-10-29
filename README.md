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

## License
`MIT License

Copyright (c) 2021 Grace Fu, Zhining He, Faiyaz Ahmed, Pengcheng Yan, Jingzeng Xie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.`
