from django.shortcuts import render
from django.http import HttpResponse

def django_view(request):
    return render(request, 'django_tag.html', {'request':request})
