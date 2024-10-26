from django.db import models

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Название')
    Genre = models.CharField(max_length=50, verbose_name='Жанр')
    Author = models.CharField(max_length=50, verbose_name='Автор')
    Publication = models.IntegerField(max_length=50, verbose_name='Год издания')
   # Status = models.CharField(max_length=50, verbose_name='Статус')

class Reader(models.Model):
    Name = models.CharField(max_length=50, verbose_name='ФИО')
    Birthday = models.DateField(max_length=50, verbose_name='Дата рождения')
    Number_phone = models.IntegerField(max_length=50, verbose_name='Номер телефона')
   # Name = models.CharField(max_length=50, verbose_name='Список выданных книг')

class Book_read(models.Model):
   # Reader_id = models.IntegerField(max_length=50, verbose_name='ID читателя')
  #  Book_id = models.IntegerField(max_length=50, verbose_name='ID книги')
    Data_received = models.DateField(max_length=50, verbose_name='Дата выдачи')
    Data_refund = models.DateField(max_length=50, verbose_name='Дата возврата')
    # Status = models.CharField(max_length=50, verbose_name='Статус')