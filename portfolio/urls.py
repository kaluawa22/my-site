from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^resume/$', views.resume, name='resume'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^indexsnake/$', views.snakeGame, name='indexsnake'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)