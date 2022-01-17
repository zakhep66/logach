from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from .views import *


urlpatterns = [
	path('', index, name="index"),
	path('staff/', StaffsView.as_view(), name="staff"),
	path('clients/', clients, name="clients"),
	path('create-staff', CreateStaff.as_view(), name="create_staff"),
]
