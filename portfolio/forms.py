from django.conf import settings
from django.contrib.auth import get_user_model
from django import forms

from .models import Portfolio, Skill, Project

class DateInput(forms.DateInput):
    input_type = 'date'

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['user']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['portfolio']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['portfolio']