from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolioapp.models import Profile, Skill, Project

class Command(BaseCommand):
    help = 'Set up initial portfolio data'
    
    def handle(self, *args, **options):
        # Create superuser if doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            
        # Create profile
        user = User.objects.filter(is_superuser=True).first()
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'bio': 'Full-stack developer passionate about creating innovative solutions.',
                'location': 'Your City, Country',
                'github_url': 'https://github.com/nabin720',
                'linkedin_url': 'https://linkedin.com/in/yourusername',
            }
        )
        
        # Create sample skills
        skills_data = [
            {'name': 'Python', 'category': 'backend', 'proficiency': 90},
            {'name': 'Django', 'category': 'backend', 'proficiency': 85},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 80},
            {'name': 'React', 'category': 'frontend', 'proficiency': 75},
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 70},
        ]
        
        for skill_data in skills_data:
            Skill.objects.get_or_create(**skill_data)
        
        self.stdout.write(self.style.SUCCESS('Portfolio setup completed!'))
