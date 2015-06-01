# -*- coding: utf-8 -*-
from django.db import models
#Comments
class Address(models.Model):

    City = models.CharField(max_length=50, db_column="City", verbose_name="City", null=False)
    Street = models.CharField(max_length=50, db_column="Street", verbose_name="Street", null=False)
    House = models.CharField(max_length=50, db_column="House", verbose_name="House", null=False)
    Phone = models.CharField(max_length=50, db_column="Phone", verbose_name="Phone", null=False)

    def get_absolute_url(self):
        return "/address/%i/" % self.pk

    class Meta:
        db_table = "Address"


class Person(models.Model):

    Name = models.CharField(max_length=50, db_column="Name", verbose_name="Name", null=False)
    Surname = models.CharField(max_length=50, db_column="Surname", verbose_name="Surname", null=False)
    Phone = models.CharField(max_length=50, db_column="Phone", verbose_name="Phone", null=False)

    class Meta:
        db_table = "Person"

class FormOfLeg(models.Model):

    Name = models.CharField(max_length=50, db_column="Name", verbose_name="Name", null=False)

    class Meta:
        db_table = "FormOfLeg"

class TypeOfSocForm(models.Model):

    Name = models.CharField(max_length=50, db_column="Name", verbose_name="Name", null=False)

    class Meta:
        db_table = "TypeOfSocForm"



class SocialFormation(models.Model):

    Name = models.CharField(max_length=50, db_column="Name", verbose_name="Name", null=False)
    DateReg = models.DateField(null=False, db_column="DateReg", verbose_name="DateReg")
    RegNumb = models.IntegerField(null=False, db_column="RegNumb", verbose_name="RegNumb")

    Address = models.ForeignKey(Address)
    Person = models.ForeignKey(Person)
    TypeOfSocForm = models.ForeignKey(TypeOfSocForm)
    FormOfLeg = models.ForeignKey(FormOfLeg)

    class Meta:
        db_table = "SocialFormation"

class Filia(models.Model):

    Name = models.CharField(max_length=50, db_column="Name", verbose_name="Name", null=False)
    DateReg = models.DateField(null=False, db_column="DateReg", verbose_name="DateReg")

    SocialFormation = models.ForeignKey(SocialFormation)
    Address = models.ForeignKey(Address)
    Person = models.ForeignKey(Person)

    class Meta:
        db_table = "Filia"



##################################
'''
class Adresa(models.Model):

    misto = models.CharField(max_length=50, db_column="misto", verbose_name="Город", null=False)
    vulicya = models.CharField(max_length=50, db_column="vulicya", verbose_name="Улица", null=False)
    budinok = models.CharField(max_length=50, db_column="budinok", verbose_name="Дом", null=False)

    def get_absolute_url(self):
        return "/adresa/%i/" % self.pk

    class Meta:
        db_table = "Adresa"

class Arbitrazhnij(models.Model):

    prizvishhe = models.CharField(max_length=50, db_column="prizvishhe", verbose_name="Фамилия", null=False)
    imya = models.CharField(max_length=50, db_column="imya", verbose_name="Имя", null=False)
    po_batkovi = models.CharField(max_length=50, db_column="po_batkovi", verbose_name="Очество", null=False)
    nomer = models.IntegerField(db_column="nomer", verbose_name="Номер", null=False)
    data_vidachi = models.DateField(db_column="data_vidachi", verbose_name="Дата выдачи", null=False)
    telefon = models.CharField(max_length=50, db_column="telefon", verbose_name="Телефон", null=False)

    Adresa = models.ForeignKey(Adresa)

    class Meta:
        db_table = "Arbitrazhnij"

class Borzhnik(models.Model):

    najmenuvannya = models.CharField(max_length=50, db_column="najmenuvannya", verbose_name="название", null=False)
    kod_edrpou = models.IntegerField(db_column="kod_edrpou", verbose_name="Код ЕДРПОУ", null=False)
    prizvishhe = models.CharField(max_length=50, db_column="prizvishhe", verbose_name="Фамилия", null=False)
    imya = models.CharField(max_length=50, db_column="imya", verbose_name="Имя", null=False)
    po_batkovi = models.CharField(max_length=50, db_column="po_batkovi", verbose_name="Очество", null=False)
    nomer_edryuofop = models.IntegerField(db_column="nomer_edryuofop", verbose_name="Номер ЕДРЮОФОП", null=False)
    vid_diyalnosti = models.CharField(max_length=50, db_column="vid_diyalnosti", verbose_name="Вид деятельности", null=False)
    forma_vlasnosti = models.CharField(max_length=50, db_column="forma_vlasnosti", verbose_name="Форма собствености", null=False)
    chastka_derzhavi = models.CharField(max_length=50, db_column="chastka_derzhavi", verbose_name="Часть государства", null=False)
    data_porush_provadzh = models.DateField(db_column="data_porush_provadzh", verbose_name="Дата возбуждения дела", null=False)
    stan_provadzhennya = models.CharField(max_length=50, db_column="stan_provadzhennya", verbose_name="Состояние дела", null=False)

    Adresa = models.ForeignKey(Adresa)
    Arbitrazh = models.ForeignKey(Arbitrazhnij)

    class Meta:
        db_table = "Borzhnik"

class Kreditor(models.Model):

    prizvishhe = models.CharField(max_length=50, db_column="prizvishhe", verbose_name="Фамилия", null=False)
    imya = models.CharField(max_length=50, db_column="imya", verbose_name="Имя", null=False)
    po_batkovi = models.CharField(max_length=50, db_column="po_batkovi", verbose_name="Отество", null=False)
    nomer_edryuofop = models.IntegerField(db_column="nomer_edryuofop", verbose_name="Номер ЕДРЮОФОП", null=False)
    telefon = models.CharField(max_length=50, db_column="telefon", verbose_name="Телефон", null=False)

    Adresa = models.ForeignKey(Adresa)

    class Meta:
        db_table = "Kreditor"

class Vimogi(models.Model):

    zagalna_suma = models.IntegerField(db_column="zagalna_suma", verbose_name="Общая сума", null=False)
    viplacheno = models.IntegerField(db_column="viplacheno", verbose_name="Выплачено", null=False)
    kinceva_data = models.DateField(db_column="kinceva_data", verbose_name="Дата выплаты", null=False)

    Kreditor = models.ForeignKey(Kreditor)
    Borzhnik = models.ForeignKey(Borzhnik)

    class Meta:
        db_table = "Vimogi"'''