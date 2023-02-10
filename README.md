instant-django
====

Instant-django is a practical sample project of Django.

Instant-django has a sample model and basic CRUD views.

You can complete a simple CRUD WebApp with a few edits and commands.

## Requirement

```
Django==2.1.1
django-crispy-forms==1.7.2
django-filter==2.0.0
pytz==2018.5
```

## Usage

Steps

1. Git clone this project
2. Edit modelfile `app/models.py`
3. Run `makemigrations` and `migrate`
4. Edit HTML files `templates/item_filter.html` and `item_detail_contents.html`

If you use it production environment, you must replace `settings.SECRET_KEY`.

## Contribution

I wrote this for Japanese python beginners.

I would appreciate if you clone this project and replace japanese code with your language for your country's python beginners.

## Licence


## Author


# start
sudo pip install virtualenv

virtualenv -p python3 venv 

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver 8080