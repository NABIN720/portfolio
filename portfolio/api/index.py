import os
import sys
from pathlib import Path

# Add the project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

import django
from django.core.wsgi import get_wsgi_application

# Initialize Django
django.setup()

# Get WSGI application
application = get_wsgi_application()

# Vercel handler
def handler(request):
    # This is complex - you need to convert Vercel request to Django request
    pass