from multiprocessing import context
from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import ProjectForms

from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    projectsObj = Project.objects.all()
    # context = {'projects': projectsList, 'number': number}
    return render(request, 'projects/projects.html', {'projectsObj': projectsObj})


def project(request, primaryKey):
    projectObj = Project.objects.get(id=primaryKey)
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectForms()

    if request.method == 'POST':
        form = ProjectForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)
# Create your views here.


def updareProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForms(instance=project)

    if request.method == 'POST':
        form = ProjectForms(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
