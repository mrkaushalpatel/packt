from django.shortcuts import render
from modelForms import ProjectForm
from modelForms.models import Project

# Create your views here.

def index(request):
    return render(request, 'modelForms/idex.html')

def listProjects(request):
    projectsList = Project.objects.all()
    return render(request, 'modelForms/listProjects.html', {'projects':projectsList})

def addProjects(request):
    form = ProjectForm()
    if form.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'modelForms/addProject.html', {'form':form})
