from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, DateTimeInput

from .models import *


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class StaffCreateForm(ModelForm):
    class Meta:
        model = Staff
        fields = ["last_name", "name_patronamic", "gender", "organization", "position", "user", "date_of_birth"]


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['password', 'last_login', 'username', 'date_joined']


class CreateStaffForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateStaffForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'mb-3 form-control'

    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['login', 'pass_field']
