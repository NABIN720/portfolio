from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField()
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-published_at']

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'"{self.text[:50]}..." - {self.author}'