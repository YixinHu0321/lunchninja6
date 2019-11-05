release: python datasource/dataprocess/database.py
release: echo "database done"
release: ./prepare.sh
release: ./prepare_match.sh
web: gunicorn lunchNinja.wsgi --log-file -
