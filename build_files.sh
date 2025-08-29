#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Create build directory if it doesn't exist
mkdir -p staticfiles_build

# Copy static files to build directory
cp -r staticfiles/* staticfiles_build/