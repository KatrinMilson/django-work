# Generated by Django 5.1.2 on 2024-10-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vxod', '0002_alter_animal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='Name',
            field=models.CharField(max_length=50, verbose_name='Кличка'),
        ),
    ]
