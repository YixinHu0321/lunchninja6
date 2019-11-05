release: python datasource/dataprocess/database.py
release: python manage.py makemigrations user_account
release: python manage.py makemigrations homepage
release: python manage.py migrate
release: python database.py
release: prepare_match.sh
web: gunicorn lunchNinja.wsgi --log-file -
