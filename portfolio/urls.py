# from django.conf.urls import url
from django.urls import re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name='index2021'),
    re_path(r'^projects/$', views.projects, name='projects'),
    re_path(r'^resume/$', views.resume, name='resume'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^indexsnake/$', views.snakeGame, name='indexsnake'),
    re_path(r'^indexnew/$', views.newHome, name='indexnew'),
    re_path(r'^passwordgen/$', views.passWordGen, name='passwordgen'),
    re_path(r'^currencyconverter/$', views.currecyConverter, name='currencyconverter'),
    re_path(r'^wcgame/$', views.wcGame, name='wcGame'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)