#!usr/bin bash

echo "Building project packages..."

pip install -r requirements.txt --upgrade

echo "Migrating Database..."
manage.py makemigrations --noinput
manage.py migrate --noinput

echo "Collecting static files..."
manage.py collectstatic --noinput --clear

echo "Build completed!"