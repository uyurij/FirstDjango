from django.db import models

# Create your models here.
class Color(models.Model):
   name = models.CharField(max_length=32, default = '')
   
class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description =  models.CharField(max_length=100, default = '')
   colors = models.ManyToManyField(to=Color, default='')


#class Work(models.Model):
#  organization = models.CharField(verbose_name='Организация', max_length=32)
#  region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
#  site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
#  position = models.CharField(verbose_name='Должность', max_length=16)
#  duties = models.TextField(verbose_name='Обязанности')
#  period = models.PositiveIntegerField(verbose_name='Время работы', default=1)




