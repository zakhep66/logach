from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.safestring import mark_safe

from . import models as m

# admin.site.site_title = 'Поле администратора'
admin.site.site_header = 'Поле администратора'


@admin.register(m.Staff)
class StaffAdmin(admin.ModelAdmin):
	"""Сотрудники"""
	list_display = ('last_name', 'name_patronamic')  # что видно о сотреднике не переходя на его страницу
	search_fields = ('last_name', 'name_patronamic')  # по каким полям реализован поиск
	readonly_fields = ('get_image', '_gender')
	exclude = ['gender', 'photo', 'login', 'pass_field', 'user']

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.photo} width="120" height="140"')

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
	readonly_fields = ('_gender',)
	exclude = ['gender']

	def get_extra(self, request, obj=None, **kwargs):
		extra = 0
		return extra


@admin.register(m.Client)
class ClientAdmin(admin.ModelAdmin):
	"""Клиенты"""
	list_display = ['last_name', 'name_patronymic']  # что видно о клиенте не переходя на его страницу
	search_fields = ('last_name', 'name_patronymic')  # по каким полям реализован поиск
	readonly_fields = ('_gender',)
	exclude = ['gender']
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


class ManagerAdminArea(admin.AdminSite):  # окружение менеджера
	site_header = 'Manager'  # надпись в хедере главной страницы и при авторизации


# admin.site.register(m.Staff, AdminPerms)
# admin.site.unregister(Group)
# admin.site.unregister(User)
manager_site = ManagerAdminArea(name='ManagerAdmin')
# manager_site.register(m.Staff)
# admin.site.register(m.City)
# admin.site.register(m.Currency)
# admin.site.register(m.Hotel)
# admin.site.register(m.BirthCertificate)
# admin.site.register(m.BuisnessProcess)
# admin.site.register(m.Client)
# admin.site.register(m.Contract)
# admin.site.register(m.ContractHasClient)
# admin.site.register(m.Country)
# admin.site.register(m.HotelCategory)
# admin.site.register(m.InternationalPassport)
# admin.site.register(m.Organization)
# admin.site.register(m.Passport)
# admin.site.register(m.Payment)
# admin.site.register(m.PlaceOfStay)
# admin.site.register(m.Position)
# admin.site.register(m.PreliminaryAgreement)
# admin.site.register(m.Staff, StaffAdmin)
# admin.site.register(m.StatusClient)
# admin.site.register(m.StatusProcess)
# admin.site.register(m.Ticket)
# admin.site.register(m.Transport)
# admin.site.register(m.TypeOfFood)
# admin.site.register(m.TypeOfRoom)
