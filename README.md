## Social Auth Example

This django application is done to demostrate social login with facebook. App simple
user facebook connection and fetches profile picture and username and displays.

### Installation

Below are bash to be excute to fully run project in development environment. 

```bash
mkdir project
cd project
git clone git@github.com:roshanshrestha01/social-login.git app
virtualenv env
source env/bin/activate
cd app
pip install -r requirements/dev.txt
python manage.py migrate
python manage.py runserver
```
