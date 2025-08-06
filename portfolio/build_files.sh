#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
mkdir -p staticfiles_build/static
python manage.py collectstatic --noinput --clear

# Run migrations (if using database)
python manage.py migrate --noinput