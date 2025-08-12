from django.contrib import admin
from .models import Profile, Skill, Project, Experience, Education, Contact
from django.core.mail import send_mail
from django.utils import timezone

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location']
    fields = ['user', 'bio', 'profile_image', 'resume', 'github_url', 'linkedin_url', 'twitter_url', 'website_url', 'location', 'phone']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'current']
    list_filter = ['current']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'replied']
    list_filter = ['replied', 'created_at']
    readonly_fields = ['created_at']

    def save_model(self, request, obj, form, change):
        # If there's a new response, send an email to the original sender
        if obj.response and (not obj.responded_at or 'response' in form.changed_data):
            send_mail(
                subject=f"Re: {obj.subject}",
                message=f"Reply of '{obj.message}' at Nabin's Portfolio \n {obj.response}",
                # message=obj.response,
                from_email='your_email@gmail.com',
                recipient_list=[obj.email],
            )
            obj.responded_at = timezone.now()
        super().save_model(request, obj, form, change)