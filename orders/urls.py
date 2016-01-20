from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout/$', views.create_order, name='create_order'),
]