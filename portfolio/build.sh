#!/bin/bash

# Build script for Vercel
echo "BUILD START"

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

# Create database and run migrations
python manage.py migrate --run-syncdb

# Create superuser (optional - only if needed)
# python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None"

echo "BUILD END"