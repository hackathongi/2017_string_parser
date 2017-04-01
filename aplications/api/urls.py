from django.conf.urls import url
from aplications.api import views

app_name = "api"
urlpatterns = [
    url(r'echo/(?P<text>[\w ]+)$', views.echo, name='echo'),
    url(r'parse/(?P<text>[\w ]+)$', views.parse, name='parse'),
]
