#!/usr/bin/env bash

cd /code/

echo "waiting for other builds to finish"

until mysqladmin -h mysql -u root -proot ping &> /dev/null; do
  echo "waiting for mysql to start ..." && sleep 10
done

echo "mysql is up"

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
