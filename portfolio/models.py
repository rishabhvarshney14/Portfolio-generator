from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    email_address = models.EmailField(max_length=254)
    phone_number = models.BigIntegerField(default=None)
    bio = models.TextField(max_length=1000, default='')
    facebook = models.URLField(max_length=200, default="")
    github = models.URLField(max_length=200, default='')
    twitter = models.URLField(max_length=200, default='')
    linkedin = models.URLField(max_length=200, default='')
    date_created = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f'Portfolio of {self.first_name} {self.last_name}'


skill_types = [
    ('WD', 'Web Devlopment'),
    ('PL', 'Programming Language'),
    ('ML', 'Machine Learning'),
    ('T', 'Tools'),
]

class Skill(models.Model):
    skill = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=2, choices=skill_types, default='PL')
    experience = models.IntegerField(default=0)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='')
    tech_stack = models.CharField(max_length=100, default='')
    live_link = models.URLField(max_length=200, default="")
    github_link = models.URLField(max_length=200, default='')
    date_created = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.name