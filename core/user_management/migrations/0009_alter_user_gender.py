# Generated by Django 4.0.5 on 2022-07-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0008_alter_user_gender_alter_user_present_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=6, null=True),
        ),
    ]
