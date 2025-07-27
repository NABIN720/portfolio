from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
import json
from datetime import datetime, timedelta
from .models import NewsArticle, Quote

def get_weather(request):
    """Get weather data from OpenWeatherMap API"""
    city = request.GET.get('city', 'kathmandu')

    api_key = settings.WEATHER_API_KEY
    
    if not settings.WEATHER_API_KEY:
        return JsonResponse({'error': 'Weather API key not configured'})
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon']
            }
            return JsonResponse(weather_data)
        else:
            return JsonResponse({'error': 'City not found'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def get_news(request):
    """Get latest news from New York Times with category filter"""

    category = request.GET.get('category', 'technology')  # default category

    # Validate allowed categories to prevent API misuse
    allowed_categories = [
        'arts', 'automobiles', 'books', 'business', 'fashion',
        'food', 'health', 'home', 'insider', 'magazine', 'movies',
        'nyregion', 'obituaries', 'opinion', 'politics', 'realestate',
        'science', 'sports', 'sundayreview', 'technology', 'theater',
        't-magazine', 'travel', 'upshot', 'us', 'world'
    ]
    if category not in allowed_categories:
        return JsonResponse({'error': f'Invalid category: {category}'}, status=400)

    api_key = getattr(settings, 'NEWS_API_KEY', None)
    if not api_key:
        return JsonResponse({'error': 'NEWS_API_KEY not set in settings.py'}, status=500)

    api_url = f'https://api.nytimes.com/svc/topstories/v2/{category}.json?api-key={api_key}'

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code != 200:
            return JsonResponse({'error': 'Failed to fetch NYT news'}, status=response.status_code)

        articles = []
        for article in data.get('results', [])[:10]:
            articles.append({
                'title': article.get('title'),
                'description': article.get('abstract'),
                'url': article.get('url'),
                'published_at': article.get('published_date'),
                'source': 'New York Times',
                'image': article['multimedia'][0]['url'] if article.get('multimedia') else None
            })

        return JsonResponse({'articles': articles})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_quote(request):
    """Get inspirational quote from free API"""
    try:
        # Using Quotable API (free)
        api_key = settings.QUOTE_API_KEY
        api_url = 'https://api.api-ninjas.com/v1/quotes'
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        
        if response.status_code == 200:
            data = response.json()
            if not data:
                return JsonResponse({'error': 'No quote found'}, status=404)
            
            quote_data = {
                'text': data[0]['quote'],
                'author': data[0]['author']
            }
            
            # Save to database
            Quote.objects.create(**quote_data)
            
            return JsonResponse(quote_data)
        else:
            # Fallback to stored quotes
            stored_quote = Quote.objects.order_by('?').first()
            if stored_quote:
                return JsonResponse({
                    'text': stored_quote.text,
                    'author': stored_quote.author
                })
            else:
                return JsonResponse({
                    'text': 'The only way to do great work is to love what you do.',
                    'author': 'Steve Jobs'
                })
    except Exception as e:
        return JsonResponse({'error': str(e)})

def get_github_stats(request):
    """Get GitHub user statistics"""
    username = request.GET.get('username', 'nabin720')
    
    try:
        # Get user info
        user_response = requests.get(f'https://api.github.com/users/{username}')
        user_data = user_response.json()
        
        # Get repositories
        repos_response = requests.get(f'https://api.github.com/users/{username}/repos?sort=updated&per_page=5')
        repos_data = repos_response.json()
        
        if user_response.status_code == 200:
            github_stats = {
                'username': user_data['login'],
                'name': user_data['name'],
                'bio': user_data['bio'],
                'public_repos': user_data['public_repos'],
                'followers': user_data['followers'],
                'following': user_data['following'],
                'avatar_url': user_data['avatar_url'],
                'recent_repos': [
                    {
                        'name': repo['name'],
                        'description': repo['description'],
                        'language': repo['language'],
                        'stars': repo['stargazers_count'],
                        'url': repo['html_url']
                    } for repo in repos_data[:5] if isinstance(repos_data, list)
                ]
            }
            return JsonResponse(github_stats)
        else:
            return JsonResponse({'error': 'GitHub user not found'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def get_apod(request):
    """Fetch NASA Astronomy Picture of the Day (APOD)"""
    date = request.GET.get('date')  # optional YYYY-MM-DD

    api_key = getattr(settings, 'NASA_API_KEY', 'DEMO_KEY')
    api_url = 'https://api.nasa.gov/planetary/apod'

    params = {
        'api_key': api_key,
    }
    if date:
        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            params['date'] = date
        except ValueError:
            return JsonResponse({'error': 'Invalid date format (use YYYY-MM-DD)'}, status=400)

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if response.status_code != 200:
            return JsonResponse({'error': data.get('error', 'Failed to fetch APOD')}, status=response.status_code)

        apod = {
            'title': data.get('title'),
            'explanation': data.get('explanation'),
            'media_type': data.get('media_type'),  # 'image' or 'video'
            'url': data.get('url'),
            'date': data.get('date'),
            'copyright': data.get('copyright', 'Public Domain')
        }
        

        return JsonResponse(apod)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
