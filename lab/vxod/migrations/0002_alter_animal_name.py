# Generated by Django 5.1.2 on 2024-10-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vxod', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]