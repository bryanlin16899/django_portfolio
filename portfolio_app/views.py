from django.shortcuts import render
from .models import Project, Project_study


def home(request):
    learn_notes = Project.objects.all()[0:15]
    study_notes = Project_study.objects.all()[0:15]
    return render(request, 'portfolio_app/home.html', {'learn_notes': learn_notes, 'study_notes': study_notes})

