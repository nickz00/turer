from django.db import models


class clients(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    pas_num = models.CharField(max_length=200)
    pas_take = models.CharField(max_length=200)
    pas_reg = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default='')
    activity = models.CharField(max_length=1000)
    zp = models.IntegerField()
    tours = models.CharField(max_length=1000)


class advertising(models.Model):
    for_person = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000, default='')
    date = models.CharField(max_length=1000, default='')


class interested(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default='')
    comment = models.CharField(max_length=1000)
