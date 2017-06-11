from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/submitProject$', views.submitProject),
    url(r'^/project/(?P<id>[0-9]+)$',views.showCase),
]
