from multiprocessing import context
from django.shortcuts import render
from .models import Eductation, Experience, Project, Blogs

def index(request):
    context = {
        'educations': Eductation.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'blogs': Blogs.objects.all(),
    }
    return render(request, 'index.html', context)