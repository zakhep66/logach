from django import forms  # для работы с формами
from django.contrib import admin
import nested_admin
from django.contrib.auth.models import Group, User
# from django.forms import ModelForm, ValidationError  # для вывода ошибки
# from PIL import Image  # для работы с картинками
from django.utils.safestring import mark_safe

from . import models as m

admin.site.register(m.PlaceOfStay)
admin.site.register(m.PreliminaryAgreement)
admin.site.register(m.StatusClient)
# admin.site.register(m.Country)


# class PlaceOfStayInline(nested_admin.NestedStackedInline):
# 	extra = 0
# 	model = m.PlaceOfStay


# class HotelInline(nested_admin.NestedStackedInline):
# 	model = m.Hotel
# 	extra = 0
# 	inlines = [PlaceOfStayInline]


class CityInline(nested_admin.NestedTabularInline):
	model = m.City
	extra = 0
	# inlines = [PlaceOfStayInline]


@admin.register(m.Country)
class CountryAdmin(nested_admin.NestedModelAdmin):
	inlines = [CityInline]


# @admin.register(m.PreliminaryAgreement)
# class PreliminaryAgreementAdmin(nested_admin.NestedModelAdmin):
# 	inlines = [PlaceOfStayInline]


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


@admin.register(m.Position)
class PositionAdmin(admin.ModelAdmin):
	list_display = ['description', 'position']


@admin.register(m.Organization)
class PositionAdmin(admin.ModelAdmin):
	pass


admin.site.register(m.Hotel)
admin.site.register(m.HotelCategory)
