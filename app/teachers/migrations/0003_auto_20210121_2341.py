# Generated by Django 3.1.5 on 2021-01-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_class_slots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='day',
        ),
        migrations.AlterField(
            model_name='class',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='start',
            field=models.DateTimeField(),
        ),
    ]