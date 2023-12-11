# Generated by Django 5.0 on 2023-12-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='email',
        ),
        migrations.RemoveField(
            model_name='details',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='details',
            name='password',
        ),
        migrations.RemoveField(
            model_name='details',
            name='username',
        ),
        migrations.AddField(
            model_name='details',
            name='city_name',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
        migrations.AddField(
            model_name='details',
            name='country_name',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
        migrations.AddField(
            model_name='details',
            name='state_name',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
    ]
