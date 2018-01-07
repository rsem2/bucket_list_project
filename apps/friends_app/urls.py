from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.list_friends),
    url(r'/add_friend/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)$', views.add_friend),
    url(r'/remove_friend/(?P<num>[0-9]+)$', views.remove),
]