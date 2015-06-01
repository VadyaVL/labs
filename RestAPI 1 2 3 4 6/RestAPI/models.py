# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django.db import models

# Категорії
class ViewEncumbrance(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Name')

    def __str__(self):
        return self.Name.encode('utf8')

    def get_absolute_url(self):
        return "/viewencumbrance/%i/" % self.pk

    def __unicode__(self):
        return self.Name

    class Meta:
        db_table = 'ViewEncumbrance'

class TypeOfEncumbrance(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Name')

    def __str__(self):
        return self.Name.encode('utf8')

    def get_absolute_url(self):
        return "/typeofencumbrance/%i/" % self.pk

    def __unicode__(self):
        return self.Name

    class Meta:
        db_table = 'TypeOfEncumbrance'

class TypeReg(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Name')

    def __str__(self):
        return self.Name.encode('utf8')

    def get_absolute_url(self):
        return "/typereg/%i/" % self.pk

    def __unicode__(self):
        return self.Name

    class Meta:
        db_table = 'TypeReg'

class TypeOfCurrency(models.Model):
    Name = models.CharField(max_length=45, null=False, db_column='Name', verbose_name='Name')

    def __str__(self):
        return  self.Name.encode('utf8')

    def get_absolute_url(self):
        return "/typeofcurrency/%i/" % self.pk

    def __unicode__(self):
        return self.Name

    class Meta:
        db_table = 'TypeOfCurrency'

# Сутності які додаємо окремо
class Person(models.Model):
    Identification = models.CharField(max_length=10, db_column='Identification', null=False, verbose_name='Ідентифікаційний номер')
    NonResidentForeigner = models.BooleanField(db_column='NonResidentForeigner', default=False, verbose_name='Не резидент')
    Name = models.CharField(max_length=100, db_column='Name', null=False, verbose_name='Ф.І.О.')
    MoreInformation = models.CharField(max_length=500, db_column='MoreInformation', null=True, verbose_name='Дод. інф.')
    Address = models.ForeignKey('Address', null=True)

    def __str__(self):
        return (self.Name + ' (' + self.Identification + ')').encode('utf8')

    def get_absolute_url(self):
        return "/person/%i/" % self.pk

    class Meta:
        db_table = 'Person'

class Address(models.Model):
    Country = models.CharField(max_length=45, db_column='Country', default='Україна', null=False, verbose_name='Країна')
    Index = models.CharField(max_length=45, db_column='Index', null=False, verbose_name='Індекс')
    Region = models.CharField(max_length=45, db_column='Region', null=False, verbose_name='Область')
    Area = models.CharField(max_length=45, db_column='Area', null=True, verbose_name='Район')
    City = models.CharField(max_length=45, db_column='City', null=False, verbose_name='Місто/н.п.')
    Street = models.CharField(max_length=45, db_column='Street', null=False, verbose_name='Вулиця')
    Home = models.CharField(max_length=45, db_column='Home', null=False, verbose_name='дім/буд.')

    def __str__(self):
        return (self.Country + ', ' + self.Region + ', ' + self.Area + ', ' + self.City).encode('utf8')

    def get_absolute_url(self):
        return "/address/%i/" % self.pk

    class Meta:
        db_table = "Address"

# На одній сторінці заповнюємо інформацію про
class Encumbrance(models.Model):
    NStatement = models.IntegerField(db_column='NStatement', null=False, verbose_name='Номер заяви', default=0)
    DateStatement = models.DateField(db_column='DateStatement', null=False, verbose_name='Дата заяви', default=now)
    TypeOfEncumbrance = models.ForeignKey(TypeOfEncumbrance, verbose_name='Тип обтяження')
    TypeReg = models.ForeignKey(TypeReg, verbose_name='Тип реєстрації')
    ViewEncumbrance = models.ForeignKey(ViewEncumbrance, verbose_name='Вид обтяження')
    Date = models.DateField(db_column='Date', null=False, verbose_name='Дата', default=now)
    AddedInfo = models.CharField(max_length=500, db_column='AddedInfo', null=True, verbose_name='Дод. інф.')
    #Обтяжувач
    WPerson = models.ManyToManyField(Person, related_name='W', verbose_name='Обтяжувач', help_text='')
    #Не обтяжувач
    SPerson = models.ManyToManyField(Person, related_name='S', verbose_name='Боржник')

    Obj = models.OneToOneField("Object", null=True)
    DocBase = models.OneToOneField("DocumentBase", null=True)
    Term = models.OneToOneField("Terms", null=True)

    def __str__(self):
        return (str(self.id) + ' ' + str(self.Date) + ' ' + self.TypeOfEncumbrance.Name).encode('utf8')

    def get_absolute_url(self):
        return "/encumbrance/%i/" % self.pk

    class Meta:
        db_table = 'Encumbrance'
##############################
class Object(models.Model):
    Name = models.CharField(max_length=45, db_column='Name', null=False, verbose_name='Назва')
    SerialNumber = models.CharField(max_length=45, db_column='SerialNumber', null=False, verbose_name='Серійний номер')
    RegNumber = models.CharField(max_length=45, db_column='RegNumber', null=False, verbose_name='Номер реєстрації')
    AddedInfoForUNMovable = models.CharField(max_length=500, db_column='AddedInfoForUNMovable', null=False, verbose_name='Дод. інф.(нерухоме)')
    #Encumbrance = models.OneToOneField(Encumbrance)

    def get_absolute_url(self):
        return "/object/%i/" % self.pk

    class Meta:
        db_table = 'Object'

class DocumentBase(models.Model):
    Name = models.CharField(max_length=45, db_column='Name', null=False, verbose_name='Назва')
    Number = models.CharField(max_length=45, db_column='Number', null=False, verbose_name='Номер')
    Date = models.DateField(db_column='Date', null=False, verbose_name='Дата', default=now)
    PublisherName = models.CharField(max_length=100, db_column='PublisherName', null=False, verbose_name='Публікатор')
    #Encumbrance = models.OneToOneField(Encumbrance)

    def get_absolute_url(self):
        return "/documentbase/%i/" % self.pk

    class Meta:
        db_table = 'DocumentBase'

class Terms(models.Model):
    SizeObligations = models.IntegerField(null=False, db_column='SizeObligations', verbose_name='Розмір облігації')
    LimitDate = models.DateField(db_column='LimitDate', verbose_name='Термін', default=now)
    AddedInfo = models.CharField(max_length=500, db_column='AddedInfo', null=False, verbose_name='Дод. інф.')
    TypeOfCurrency = models.ForeignKey(TypeOfCurrency)
    #Encumbrance = models.OneToOneField(Encumbrance)

    def get_absolute_url(self):
        return "/terms/%i/" % self.pk

    class Meta:
        db_table = 'Terms'
