from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'classhome': "nav-current"}
    return render(request, 'portfolio/index.html', context)

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
