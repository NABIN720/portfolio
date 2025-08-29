from django.core.handlers.wsgi import WSGIHandler
import os
import sys

# Add your project to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')

# Create Django application
application = WSGIHandler()

def handler(request, response):
    """
    This function handles every request and passes it to Django
    """
    # Convert Vercel request to WSGI format
    environ = {
        'REQUEST_METHOD': request.method,
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query_string,
        'SERVER_NAME': 'vercel',
        'SERVER_PORT': '80',
        'wsgi.input': request.body,
    }
    
    # Add headers
    for key, value in request.headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value
    
    # Response callback
    def start_response(status, headers):
        response.status = status
        for key, value in headers:
            response.set_header(key, value)
    
    # Pass to Django
    result = application(environ, start_response)
    response.body = b''.join(result)
    return response