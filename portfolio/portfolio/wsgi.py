import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings_vercel')

application = get_wsgi_application()

# Vercel serverless function handler
def handler(request, context):
    return application(request, context)

app = application