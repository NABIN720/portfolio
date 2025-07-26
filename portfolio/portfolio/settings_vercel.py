from .settings import *
import os

# Vercel-specific settings
DEBUG = False
ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'localhost', '127.0.0.1']

# Database - Use SQLite for simplicity on Vercel
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite3',  # Vercel's writable directory
    }
}

# Static files configuration for Vercel
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# CORS settings for API endpoints
CORS_ALLOWED_ORIGINS = [
    "https://your-app-name.vercel.app",  # Replace with your actual domain
]

# Environment variables
SECRET_KEY = os.environ.get('SECRET_KEY', '')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY', '')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY', '')