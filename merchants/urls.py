from django.conf.urls import url

from merchants import views

urlpatterns = [
    url(r'^$', views.merchants, name='merchants'),
    url(r'^(?P<merchant_name>.+)/(?P<pk>\d+)/$', views.merchant, name='merchant'),
]
