from django.conf.urls import url
from authen import views

app_name = 'authen'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]