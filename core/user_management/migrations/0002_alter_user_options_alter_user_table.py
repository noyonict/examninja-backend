# Generated by Django 4.0.5 on 2022-06-25 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('date_joined',), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
