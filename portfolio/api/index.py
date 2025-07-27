import os
from django.core.asgi import get_asgi_application
from mangum import Mangum

# Set settings for production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings_vercel")

# Django application
application = get_asgi_application()

# Wrap it with Mangum for AWS Lambda (used by Vercel internally)
handler = Mangum(application)
