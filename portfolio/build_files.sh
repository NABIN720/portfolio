#!/bin/bash

# Install dependencies using the correct Python version
/opt/buildhome/python*/bin/pip install -r requirements.txt

# Set Python path explicitly
PYTHON_PATH=$(find /opt/buildhome/python*/bin -name python | head -1)

# Run Django commands
$PYTHON_PATH manage.py collectstatic --noinput --clear
$PYTHON_PATH manage.py migrate --noinput