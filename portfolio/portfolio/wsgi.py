import os
import sys
from django.core.wsgi import get_wsgi_application


# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
