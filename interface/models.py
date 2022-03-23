# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


USER_GENDER = (
    (1, 'мужской'),
    (0, 'женский'),
)

USER_PERM = (
    ('super_group', 'super_group'),
    ('manager', 'manager'),
    ('agent', 'agent'),
    ('accountant', 'accountant'),
)


class BirthCertificate(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=10)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client')
    place_of_birth = models.CharField(max_length=45)
    date_of_issue = models.DateField()
    second_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    patronamic = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    date_of_birth = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Свидетельство о рождении'


class BuisnessProcess(models.Model):
    idbuisness_process = models.AutoField(db_column='idBuisness_process', primary_key=True)  # Field name made lowercase.
    contract = models.ForeignKey('Contract', models.DO_NOTHING, db_column='contract')
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='ticket')
    status_process = models.ForeignKey('StatusProcess', models.DO_NOTHING, db_column='status_process')
    payment = models.IntegerField()
    preliminary_agreemen = models.IntegerField()
    date_of_creation = models.DateField()
    update_date = models.DateField()

    class Meta:
        verbose_name = 'Бизнес процесс'


class City(models.Model):
    idcity = models.AutoField(db_column='idCity', primary_key=True)  # Field name made lowercase.
    country = models.ForeignKey('Country', models.DO_NOTHING, db_column='country')
    city_name = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Город'

    def __str__(self):
        return self.city_name


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    status = models.ForeignKey('StatusClient', models.DO_NOTHING, db_column='status', verbose_name="статус")
    last_name = models.CharField(max_length=45, verbose_name="фамилия")
    name_patronymic = models.CharField(max_length=100, verbose_name="имя отчество")
    date_of_birtch = models.DateField(verbose_name="дата рождения")
    gender = models.IntegerField(verbose_name="пол", choices=USER_GENDER)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.last_name} {self.name_patronymic}"


class Contract(models.Model):
    idcontract = models.AutoField(db_column='idContract', primary_key=True)  # Field name made lowercase.
    currency = models.ForeignKey('Currency', models.DO_NOTHING, db_column='currency', verbose_name="Валюта", related_name="Валюта")
    date_of_signing = models.DateField(verbose_name="Дата подписания")
    sum = models.CharField(max_length=10, verbose_name="Сумма")

    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договора"


class ContractHasClient(models.Model):
    contract = models.OneToOneField(Contract, models.DO_NOTHING, primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        verbose_name = 'ContractHasClient'


class Country(models.Model):
    idcountry = models.AutoField(db_column='idCountry', primary_key=True)  # Field name made lowercase.
    country = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Страна'


class Currency(models.Model):
    idcurrency = models.AutoField(db_column='idCurrency', primary_key=True)  # Field name made lowercase.
    name_currency = models.CharField(max_length=30, verbose_name="Наименование валюты")
    code = models.CharField(max_length=45, verbose_name="Код валюты")
    rate = models.CharField(max_length=45, verbose_name="Курс")
    update_date = models.DateField(verbose_name="Дата обновления курса валют")

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

    def __str__(self):
        return self.name_currency

class Hotel(models.Model):
    idhotel = models.AutoField(db_column='idHotel', primary_key=True)  # Field name made lowercase.
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city', verbose_name="Город")
    hotel_category = models.ForeignKey('HotelCategory', models.DO_NOTHING, db_column='hotel_category', verbose_name="Категория отеля")
    hotel = models.CharField(max_length=45, verbose_name="Отель")
    address = models.CharField(max_length=100, verbose_name="Адрес")

    class Meta:
        verbose_name = 'Отель'

    def __str__(self):
        return self.hotel


class HotelCategory(models.Model):
    idhotel_category = models.AutoField(db_column='idHotel_category', primary_key=True)  # Field name made lowercase.
    hotel_category = models.CharField(max_length=45)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория отеля'


class InternationalPassport(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=10)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    place_of_birth = models.CharField(max_length=45)
    state_code = models.CharField(max_length=10)
    date_of_issue = models.DateField()
    expiration_date = models.DateField()
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    patronamic = models.CharField(max_length=45, blank=True, null=True)
    gender = models.IntegerField()
    date_of_birth = models.DateField()

    class Meta:
        verbose_name = 'Загран паспорт'


class Organization(models.Model):
    idorganization = models.AutoField(primary_key=True)
    organization = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Организация'

    def __str__(self):
        return self.organization


class Passport(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=10, verbose_name="серия номер")
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    date_of_birth = models.DateField(verbose_name="дата рождения")
    place_of_birth = models.CharField(max_length=45, blank=True, null=True, verbose_name="место рождения")
    issued_by = models.CharField(max_length=45, verbose_name="выдано")
    date_issued = models.DateField(verbose_name="дата выдачи")
    expiration_date = models.DateField(verbose_name="дата окончания")
    last_name = models.CharField(max_length=45, verbose_name="фамилия")
    first_name = models.CharField(max_length=45, verbose_name="имя")
    patronamic = models.CharField(max_length=45, blank=True, null=True, verbose_name="отчество")
    gender = models.IntegerField(verbose_name="пол", choices=USER_GENDER)

    class Meta:
        verbose_name = 'Паспорт'

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronamic}"


class Payment(models.Model):
    idpayment = models.AutoField(db_column='idPayment', primary_key=True)  # Field name made lowercase.
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    date = models.DateField()
    sum_in_rub = models.IntegerField()

    class Meta:
        verbose_name = 'Оплата'


class PlaceOfStay(models.Model):
    idplace_of_stay = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotel', verbose_name="Отель")
    preliminary_agreement = models.ForeignKey('PreliminaryAgreement', models.DO_NOTHING, db_column='preliminary_agreement', verbose_name="Предварительное соглашение")
    type_of_food = models.ForeignKey('TypeOfFood', models.DO_NOTHING, db_column='type_of_food', verbose_name="Тип питания")
    type_of_room = models.ForeignKey('TypeOfRoom', models.DO_NOTHING, db_column='type_of_room', verbose_name="Тип комнаты")
    start_of_trip = models.DateField(verbose_name="Дата въезда")
    finish_of_trip = models.DateField(verbose_name="Дата выезда")

    class Meta:
        verbose_name = 'Место остановки'

    def __str__(self):
        return "Место прибывания"


class Position(models.Model):
    idposition = models.AutoField(primary_key=True)
    position = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = 'Должность'

    def __str__(self):
        return self.position


class PreliminaryAgreement(models.Model):
    idpreliminary_agreement = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization', verbose_name="Организация")
    staff = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staff', verbose_name="Сотрудник")
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', verbose_name="Клиент")
    date = models.DateField(verbose_name="Дата оформления")
    start_of_trip = models.DateField(verbose_name="Дата начала поездки")
    finish_of_trip = models.DateField(verbose_name="Дада окончания поездки")
    number_of_participants = models.IntegerField(verbose_name="Количество участников")

    class Meta:
        verbose_name = "Предварительное соглашение"
        verbose_name_plural = "Предварительные соглашения"

    def clean(self):
        if self.staff.organization != self.organization:
            raise ValidationError(('Неверно указана организация'))

    def __str__(self):
        return f'Предварительное соглашение с {self.client}'


class Staff(models.Model):
    idstaff = models.AutoField(primary_key=True)
    position = models.ForeignKey('Position', models.DO_NOTHING, db_column='position', verbose_name="должность", default='1')
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organization', verbose_name="организация", default='1')
    login = models.CharField(max_length=45, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, verbose_name="Фамилия")
    name_patronamic = models.CharField(max_length=45, verbose_name="Имя Отчество")
    gender = models.IntegerField(verbose_name="пол", choices=USER_GENDER)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="дата рождения")
    photo = models.ImageField(blank=True, null=True, verbose_name="фото")
    user = models.OneToOneField(User, models.CASCADE, db_column='user', blank=True, null=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f'{self.last_name} {self.name_patronamic}'


class StatusClient(models.Model):
    idstatus = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=45, verbose_name="статус")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="описание")

    class Meta:
        verbose_name = 'Статус клиента'

    def __str__(self):
        return self.status


class StatusProcess(models.Model):
    idstatus = models.AutoField(db_column='idStatus', primary_key=True)  # Field name made lowercase.
    status_process = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Статус процесса'


class Ticket(models.Model):
    idticket = models.AutoField(db_column='idTicket', primary_key=True)  # Field name made lowercase.
    transport = models.ForeignKey('Transport', models.DO_NOTHING, db_column='transport')
    travel_card = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    transfer = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Билет'


class Transport(models.Model):
    idtransport = models.AutoField(db_column='idTransport', primary_key=True)  # Field name made lowercase.
    transport = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Транспорт'


class TypeOfFood(models.Model):
    idtype_of_food = models.AutoField(primary_key=True)
    type_of_food = models.CharField(max_length=45)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип питания'


class TypeOfRoom(models.Model):
    idtype_of_room = models.AutoField(primary_key=True)
    type_of_room = models.CharField(max_length=45)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип комнаты'


class Visa(models.Model):
    number_visa = models.CharField(primary_key=True, max_length=20)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    second_name = models.CharField(max_length=45)
    name_patronamic = models.CharField(db_column='Name_Patronamic', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_of_issue = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        verbose_name = 'VISA'
