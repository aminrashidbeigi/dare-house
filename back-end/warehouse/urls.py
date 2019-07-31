from django.conf.urls import url

from . import views

app_name = 'ponisha'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
