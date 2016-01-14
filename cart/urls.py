from django.conf.urls import url

from cart import views

urlpatterns = [
    url(r'^$', views.view_cart, name='view_cart'),
    url(r'^add/$', views.add_to_cart, name="add_cart"),
    url(r'^remove/$', views.remove_item, name="remove_item"),
    url(r'^update/$', views.update_cart, name="update_cart"),
]