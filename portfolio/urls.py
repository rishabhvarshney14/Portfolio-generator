from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_portfolio/', views.createPortfolio, name='create_portfolio'),
    path('edit_portfolio/', views.editPortfolio, name='edit_portfolio'),
    path('add_project/', views.addProject, name='add_project'),
    path('add_skill/', views.addSkill, name='add_skill'),
    path('error/', views.showError, name='show_error'),
    path('<username>/', views.showPortfolio, name='show_portfolio'),
    path('<username>/projects/', views.showProjects, name='show_projects'),
]