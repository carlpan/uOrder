from django.conf.urls import url

from merchants import views

urlpatterns = [
    url(r'^$', views.merchants, name='merchants'),

]
