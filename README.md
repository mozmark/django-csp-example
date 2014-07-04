django-csp-example
==================

An example project for playing with django-csp changes

```bash 
git clone https://github.com/mozmark/django-csp-example.git
git clone https://github.com/mozmark/django-csp.git
virtualenv venv
source venv/bin/activate
pip install django
pip install django-jinja
cd django-csp
python setup.py install
cd ../django-csp-example
python manage.py runserver 8080
```

Then just point your browser at http://localhost:8080

you can play with the template in csptest/templates 
