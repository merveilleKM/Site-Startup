from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def apropos(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def stage(request):
    return render(request, 'stage.html')

def formation(request):
    return render(request, 'formation.html')
# Create your views here.
