# Generated by Django 3.1.5 on 2021-01-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_activity_calendarcredentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarcredentials',
            name='credentials',
            field=models.BinaryField(),
        ),
    ]
