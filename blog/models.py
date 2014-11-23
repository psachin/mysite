from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog(models.Model):
    """Basic blog elements."""
    name = models.TextField()   # Blog name
    tagline = models.TextField() # Blog tagline

    def __str__(self):
        return self.name


class Category(models.Model):
    """Blog post categories."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post elements."""
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



