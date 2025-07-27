#!/bin/bash
echo "BUILD START"
python manage.py collectstatic --noinput
python manage.py migrate --noinput
echo "BUILD END"
