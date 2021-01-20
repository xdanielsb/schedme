# Generated by Django 3.1.5 on 2021-01-20 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_video_call', models.CharField(max_length=2000)),
                ('topic', models.CharField(max_length=30)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('day', models.DateField()),
                ('student', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
        ),
    ]
