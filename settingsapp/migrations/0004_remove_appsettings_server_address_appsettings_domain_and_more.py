# Generated by Django 4.2.7 on 2023-11-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settingsapp', '0003_appsettings_default_password_appsettings_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appsettings',
            name='server_address',
        ),
        migrations.AddField(
            model_name='appsettings',
            name='domain',
            field=models.CharField(default='21321', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appsettings',
            name='user',
            field=models.CharField(default='123543', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='search_base',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='appsettings',
            name='user_dn',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
