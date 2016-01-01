from django.conf.urls import url
from authen import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]
