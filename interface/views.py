from datetime import datetime

import requests
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import *
from .models import *


class Login(LoginView):
	template_name = "interface/login.html"
	form_class = AuthUserForm


# success_url = reverse_lazy("employees")


def index(request):
	search_query = request.GET.get('search', '')

	if search_query:
		staff = Staff.objects.filter(fio__icontains=search_query)
	else:
		staff = Staff.objects.all()
	return render(request, 'interface/index.html', {'staff': staff})


# def staff(request, id):
# 	error = ''
# 	staff = Staff.objects.get(id=id)
# 	if request.method == 'POST':
# 		form_staff = StaffCreateForm(request.POST, instance=staff)
# 		if form_staff.is_valid():
# 			with transaction.atomic():
# 				person = Staff.objects.get(id=id)
# 				user = User.objects.get(id=person.user.id)
# 				staff_instance = form_staff.save(commit=False)
# 				staff_instance.user = user
# 				staff_instance.save()
# 			return redirect('staff')
# 		else:
# 			error = 'Форма заполнена некорректно'
# 	user = User.objects.get(id=staff.user.id)
# 	positions = Position.objects.all()
# 	organizations = Organization.objects.all()
# 	return render(request, 'interface/staff.html', {'staff': staff, 'positions': positions,
# 	                                                'organizations': organizations, 'user': user,
# 	                                                'error': error})


def clients(request):
	clients = Client.objects.all()
	return render(request, 'interface/clients.html', {'clients': clients})


# def create_staff(request):
# 	error = ''
# 	double = ''
# 	if request.method == 'POST':
# 		check_unique = Staff.objects.filter(name_patronamic=request.POST['name_patronamic'],
# 		                                    last_name=request.POST['last_name'],
# 		                                    date_of_birth=request.POST['date_of_birth'],
# 		                                    position=request.POST['position']).exists()
# 		if check_unique:
# 			double = Staff.objects.filter(last_name=request.POST['last_name'], name_patronamic=request.POST['name_patronamic'],
# 			                              date_of_birth=request.POST['date_of_birth'], position=request.POST['position']).latest('id')
#
# 		if not check_unique or 'double' in request.POST:
# 			req = request.POST.copy()
# 			if 'double' in request.POST:
# 				req.pop('double')
# 			last_id = User.objects.latest('id').id
# 			generate_username = 'user' + str(last_id)
# 			form_user = UserCreateForm(
# 				{'password': 'pbkdf2_sha256$260000$PSBgh7lmKJVRrRhjCbLKOy$PU2iKYptNwdOEquhRHuK2qxq9GbPBrPn/8NHOed9Jxg=',
# 				 'last_login': str(datetime.now()), 'username': generate_username,
# 				 'date_joined': str(datetime.now())})
# 			form_staff = StaffCreateForm(req)
#
# 			if form_user.is_valid() and form_staff.is_valid():
# 				with transaction.atomic():
# 					user_instance = form_user.save(commit=False)
# 					form_user.save()
# 					employee_instance = form_staff.save(commit=False)
# 					employee_instance.user = user_instance
# 					employee_instance.save()
# 				return redirect('employees')
# 			else:
# 				error = str(form_user.errors) + str(form_staff.errors)
# 		else:
# 			error = 'Сотрудник с такими же данными уже существует. Выберите филиал и повторите отправку данных, если всё же хотите внести его в базу'
#
# 	positions = Position.objects.all()
# 	organizations = Organization.objects.all()
# 	return render(request, 'interface/create_staff.html',
# 	              {'positions': positions, 'organizations': organizations, 'error': error, 'init': double})

# def create_staff(request):
# 	if request.method == 'POST':
# 		form = CreateStaffForm(requests.post)
# 		if form.is_valid():
# 			try:
# 				form.save()
# 				return redirect('index')
# 			except:
# 				form.add_error(None, 'Ошибка добавления пользователя')
#
# 	if request.method == 'GET':
# 		form = CreateStaffForm()
# 		return render(request, 'interface/create_staff.html', {'form': form})


class CreateStaff(View):
	def get(self, request):
		form = CreateStaffForm()
		return render(request, 'interface/create_staff.html', {'form': form})

	def post(self, request):
		form = CreateStaffForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('index')
			except:
				form.add_error(None, 'Ошибка добавления пользователя')


class StaffsView(View):
	def get(self, request):
		return render(request, 'interface/staff.html', {''})
