release: python datasource/dataprocess/database2.py
release: echo "database done"
release: python makemigrations homepage
release: python makemigrations user_account
release: python manage.py migrate
release: echo "migrate done"
web: gunicorn lunchNinja.wsgi --log-file -
