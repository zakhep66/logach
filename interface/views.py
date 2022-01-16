from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from interface.forms import *
from interface.models import *


class Login(LoginView):
    template_name = "interface/login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy("main_page")


def get_staffs(request):
    staffs = Staff.objects.all()
    return staffs


class UsersView(View):
    def get(self, request):
        return render(request, 'interface/main_page.html')
