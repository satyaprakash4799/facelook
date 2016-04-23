"""URL configuration for Users."""
from django.conf.urls import url
from .views import register, login, logout, account


urlpatterns = [
    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^account/$', account),

]
