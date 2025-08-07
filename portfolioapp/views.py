from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Profile, Project, Skill, Experience, Education, Contact
from .forms import ContactForm
import json

def home(request):
    try:
        profile = Profile.objects.get(user__is_superuser=True)
    except Profile.DoesNotExist:
        profile = None
    
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'portfolioapp/home.html', context)

def about(request):
    try:
        profile = Profile.objects.get(user__is_superuser=True)
    except Profile.DoesNotExist:
        profile = None
    
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'portfolioapp/about.html', context)

def projects(request):
    all_projects = Project.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'projects': all_projects,
        'skills': skills,
    }
    return render(request, 'portfolioapp/projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolioapp/project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    
    return render(request, 'portfolioapp/contact.html', {'form': form})

def productivity_dashboard(request):
    """Dashboard with integrated APIs for productivity"""
    return render(request, 'portfolioapp/productivity.html')
