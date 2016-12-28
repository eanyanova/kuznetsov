from django.conf.urls import url
from . import views


app_name = 'users'
urlpatterns = [
    url(r'^$', views.UserListView.as_view(), name='list'),
    url(r'^create/$', views.UserCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.UserUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.UserDeleteView.as_view(), name='delete'),
]