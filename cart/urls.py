from django.conf.urls import url

from cart import views

urlpatterns = [
    url(r'^$', views.view_cart, name='view_cart'),
    url(r'^add/$', views.add_to_cart, name="add_cart"),
]