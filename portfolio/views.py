from django.shortcuts import render


# Create your views here.

# def index(request):
#     context = {'classhome': "nav-current"}
#     return render(request, 'portfolio/index.html', context)

def index(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/index2021.html', context)

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
