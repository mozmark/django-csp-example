from django.shortcuts import render

def jinja_view(request):
    return render(request, 'jinja_tag.jinja', {'request':request})

