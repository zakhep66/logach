from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *


urlpatterns = [
	path('login/', Login.as_view(), name='login_page'),
	path('main-page/', UsersView.as_view(), name='main_page'),
	path('logout', LogoutView.as_view(next_page="login_page"), name='logout_page'),
]
