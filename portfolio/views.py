from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

# def index(request):
#     context = {'classhome': "nav-current"}
#     return render(request, 'portfolio/index.html', context)

def index(request):
    # context = {'classhome': "nav-current"}
    form = ContactForm()
    return render(request, 'portfolio/index2021.html', {'form': form})

def resume(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/resume.html', context)
def contact(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/contact.html', context)


def projects(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/projects.html', context)

def snakeGame(request):
    context = {'classSnakeGame': "snake-current"}
    return render(request, 'portfolio/indexsnake.html', context)

def newHome(request):
    context = {'classNewHome': "newHome-current"}
    return render(request, 'portfolio/indexnew.html', context)

def passWordGen(request):
    context = {'classPasswordGen': "passWordGen-current"}
    return render(request, 'portfolio/passwordgen.html', context)
def currecyConverter(request):
    context = {'classCurrencyConverter': "currencyConverter-current"}
    return render(request, 'portfolio/currencyconverter.html', context)

def wcGame(request):
    context = {'classwcGame': "wcGame-current"}
    return render(request, 'portfolio/WCGameIndex.html', context)