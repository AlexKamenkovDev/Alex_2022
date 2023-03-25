from django.shortcuts import render
from .models import Project


# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pc):
    project = Project.objects.get(pc=pc)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
