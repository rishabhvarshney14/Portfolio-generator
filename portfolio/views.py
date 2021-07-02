from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

from .forms import PortfolioForm, ProjectForm, SkillForm
from .models import Portfolio, Project, Skill

def get_portfolio(user=None, username=None):
    if user == None:
        try:
            userObj = get_user_model()
            user = userObj.objects.get(username=username)
        except userObj.DoesNotExist:
            return False
    try:
        return Portfolio.objects.get(user = user)
    except Portfolio.DoesNotExist:
        return False

def home(request):
    user_auth = request.user.is_authenticated
    have_portfolio = False
    if user_auth:
        have_portfolio = get_portfolio(request.user)

    context = {
        'user_auth': user_auth,
        'have_portfolio':  have_portfolio,
    }
    return render(request, 'home/home.html', context=context)

def createPortfolio(request):
    if request.user.is_authenticated:
        form = PortfolioForm

        if get_portfolio(request.user):
            return redirect('home')
            
        if request.method == 'POST':
            form = PortfolioForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('add_project')
        context = {
            'user_auth': True,
            'form': form
        }
        return render(request, 'home/create_portfolio.html', context)
    return redirect('account_login')

def editPortfolio(request):
    if request.user.is_authenticated:
        portfolio = get_portfolio(request.user)
        if portfolio == False:
            return redirect('home')

        form = PortfolioForm(request.POST or None, instance=portfolio)
            
        if request.method == 'POST':
            form = PortfolioForm(request.POST, instance=portfolio)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('add_project')
        context = {
            'user_auth': True,
            'form': form,
            'have_portfolio': True
        }
        return render(request, 'home/create_portfolio.html', context)
    return redirect('account_login')

def addProject(request):
    if request.user.is_authenticated:
        form = ProjectForm
        portfolio = get_portfolio(request.user)
        
        if portfolio == False:
            return redirect('create_portfolio')

        projects = Project.objects.filter(portfolio=portfolio)
        project_len = len(projects)
    
        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.instance.portfolio = portfolio
                form.save()
                return redirect('add_project')
        context = {
            'user_auth': True,
            'have_portfolio': True,
            'projects': projects,
            'project_len': project_len,
            'form': form,
        }
        return render(request, 'home/add_project.html', context)
    return redirect('account_login')

def addSkill(request):
    if request.user.is_authenticated:
        form = SkillForm
        portfolio = get_portfolio(request.user)
        
        if portfolio == False:
            return redirect('create_portfolio') 
        
        skills = Skill.objects.filter(portfolio=portfolio)
        skill_len = len(skills)
    

        if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                form.instance.portfolio = portfolio
                form.save()
                return redirect('add_skill')
        context = {
            'user_auth': True,
            'have_portfolio': True,
            'skills': skills,
            'skill_len': skill_len,
            'form': form,
        }
        return render(request, 'home/add_skill.html', context)
    return redirect('account_login')

def showPortfolio(request, username):
    if request.user.is_authenticated:
        is_user = request.user.username == username
    else:
        is_user = False
    portfolio = get_portfolio(username=username)
    if portfolio == False:
        return redirect('create_portfolio')
    bio = portfolio.bio.split('\n')
    have_skills = True
    skills = Skill.objects.filter(portfolio=portfolio)    
    
    if len(skills) < 1:
        have_skills = False

    context = {
        'portfolio': portfolio,
        'username': username,
        'bio': bio,
        'is_user': is_user,
        'skills': skills,
        'have_skills': have_skills
    }
    return render(request, 'portfolio/bio.html', context=context)

def showProjects(request, username):
    if request.user.is_authenticated:
        is_user = request.user.username == username
    else:
        is_user = False
    portfolio = get_portfolio(username=username)
    if portfolio == False:
        return redirect('create_portfolio')
    projects = Project.objects.filter(portfolio=portfolio)
    have_projects = True
    if len(projects) < 1:
        have_projects = False
    context = {
        'portfolio': portfolio,
        'projects': projects,
        'username': username,
        'is_user': is_user,
        'have_projects': have_projects,
    }
    return render(request, 'portfolio/projects.html', context=context)

def showError(request):
    return render(request, 'home/error.html')