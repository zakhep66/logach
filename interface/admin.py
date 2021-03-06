from django import forms  # для работы с формами
from django.contrib import admin
import nested_admin
from django.contrib.auth.models import Group, User
# from django.forms import ModelForm, ValidationError  # для вывода ошибки
# from PIL import Image  # для работы с картинками
from django.utils.safestring import mark_safe

from . import models as m


class PlaceOfStayInline(nested_admin.NestedStackedInline):
	model = m.PlaceOfStay
	extra = 0
# inlines = [
# 	HotelInline,
# ]


class HotelInline(nested_admin.NestedStackedInline):
	model = m.Hotel
	extra = 0
	inlines = [PlaceOfStayInline]


class ContractInline(nested_admin.NestedStackedInline):
	model = m.Contract
	extra = 0


@admin.register(m.Currency)
class CurrencyAdmin(nested_admin.NestedModelAdmin):
	inlines = [ContractInline]


@admin.register(m.PreliminaryAgreement)
class PreliminaryAgreementAdmin(nested_admin.NestedModelAdmin):
	inlines = [PlaceOfStayInline]


@admin.register(m.Staff)
class StaffAdmin(admin.ModelAdmin):
	"""Сотрудники"""
	list_display = ('last_name', 'name_patronamic')  # что видно о сотруднике не переходя на его страницу
	search_fields = ('last_name', 'name_patronamic')  # по каким полям реализован поиск
	readonly_fields = ('get_photo',)
	exclude = ['login', 'pass_field', 'user']

	def get_photo(self, obj):
		return mark_safe(f'<img src={obj.photo.url} width="auto" height="140"')

	# form = StaffAdminForm

	def has_add_permission(self, request):
		return True

	def has_delete_permission(self, request, obj=None):
		return False

	def has_view_permission(self, request, obj=None):
		return True

	def has_change_permission(self, request, obj=None):
		return True


# @admin.register(m.Passport) # регистрация поля в админке не нужна если нужно видеть паспорт только в поле клиента
class PassportAdmin(admin.ModelAdmin):

	def has_add_permission(self, request):
		return True

	def has_delete_permission(self, request, obj=None):
		return False

	def has_view_permission(self, request, obj=None):
		return True

	def has_change_permission(self, request, obj=None):
		return True


class PassportInline(admin.StackedInline):
	model = m.Passport
	extra = 0


@admin.register(m.Client)
class ClientAdmin(admin.ModelAdmin):
	"""Клиенты"""
	list_display = ['last_name', 'name_patronymic']  # что видно о клиенте не переходя на его страницу
	search_fields = ('last_name', 'name_patronymic')  # по каким полям реализован поиск
	inlines = [
		PassportInline,
	]

	def has_add_permission(self, request):
		return True

	def has_delete_permission(self, request, obj=None):
		return False

	def has_view_permission(self, request, obj=None):
		return True

	def has_change_permission(self, request, obj=None):
		return True

# class ContractForm(forms.ModelForm):
# 	def __init__(self, *args, **kwargs):
# 		super(ContractForm, self).__init__(*args, **kwargs)
# 		self.fields['sum'].help_text = "New Help Text"
#
# 		class Meta:
# 			model = m.Contract
#
#
# class ContractAdminForm(admin.ModelAdmin):
# 	form = ContractForm
#
#
# admin.site.register(m.Contract, ContractAdminForm)


# admin.site.register(m.PlaceOfStay)
# admin.site.register(m.Staff, StaffAdmin)
# admin.site.unregister(Group)
# admin.site.unregister(User)
# admin.site.register(m.City)
# admin.site.register(m.Currency)
# admin.site.register(m.Hotel)
# admin.site.register(m.BirthCertificate)
# admin.site.register(m.BuisnessProcess)
# admin.site.register(m.Client)
# admin.site.register(m.Contract)
# admin.site.register(m.ContractHasClient)
admin.site.register(m.Country)
# admin.site.register(m.HotelCategory)
# admin.site.register(m.InternationalPassport)
admin.site.register(m.Organization)
admin.site.register(m.Passport)
# admin.site.register(m.Payment)
admin.site.register(m.Position)
# admin.site.register(m.PreliminaryAgreement)
# admin.site.register(m.Staff, StaffAdmin)
admin.site.register(m.StatusClient)
admin.site.register(m.StatusProcess)
# admin.site.register(m.Ticket)
# admin.site.register(m.Transport)
# admin.site.register(m.TypeOfFood)
# admin.site.register(m.TypeOfRoom)
