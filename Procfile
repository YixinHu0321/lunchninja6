release: python datasource/dataprocess/database2.py
release: python makemigrations homepage
release: python makemigrations user_account
release: python manage.py migrate
release: echo "database done"
release: ./prepare_match.sh
web: gunicorn lunchNinja.wsgi --log-file -
