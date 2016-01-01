from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^account/login/$', views.user_login, name='login'),
    url(r'^account/logout/$', views.user_logout, name='logout'),
]
