from django.db import models

class Color(models.Model):
   name = models.CharField(max_length=32, default = '')

   def __repr__(self):
        return f'Color({self.name})'
   
   
class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description =  models.CharField(max_length=200, default = 'Описание элемента')
   colors = models.ManyToManyField(to=Color)

   def __repr__(self):
        return f'Item({self.name})'
   

#class Work(models.Model): # создаем собственную модель Work, взято из конспекта Модели+ORM=данные
#  organization = models.CharField(verbose_name='Организация', max_length=32)
#  region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
#  site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
#  position = models.CharField(verbose_name='Должность', max_length=16)
#  duties = models.TextField(verbose_name='Обязанности')
#  period = models.PositiveIntegerField(verbose_name='Время работы', default=1)

#  def __repr__(self):
#       return f'Work({self.name})'




