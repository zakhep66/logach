from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from .views import *


urlpatterns = [
	path('', index, name="index"),
	path('staff/', staff, name="staff"),
	path('clients/', clients, name="clients"),
	path('create-staff', create_staff, name="create_staff"),
]
