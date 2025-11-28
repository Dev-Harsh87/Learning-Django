from django.http import HttpResponse
from django.shortcuts import *

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request=request, template_name='about.html')


def contact(request):
    return render(request, 'contact.html')