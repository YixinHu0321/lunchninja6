release: python manage.py migrate
release: echo "database done"
release: ./prepare_match.sh
web: gunicorn lunchNinja.wsgi --log-file -
