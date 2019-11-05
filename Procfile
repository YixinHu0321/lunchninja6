release: python datasource/dataprocess/database.py
release: python manage.py makemigrations user_account
release: python manage.py makemigrations homepage
release: python manage.py migrate
release: python create_users.py
release: python create_userrequests.py
web: gunicorn lunchNinja.wsgi --log-file -
