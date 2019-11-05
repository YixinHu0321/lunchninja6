# rm -f db.sqlite3 #
psql -c "DROP DATABASE lunchninja;"
psql -c "CREATE DATABASE lunchninja;"
rm -rf homepage/migrations
rm -rf user_account/migrations
# python datasource/dataprocess/database.py
python datasource/dataprocess/database2.py
python manage.py makemigrations homepage
python manage.py makemigrations user_account
python manage.py migrate
