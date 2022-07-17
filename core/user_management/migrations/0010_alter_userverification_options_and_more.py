# Generated by Django 4.0.5 on 2022-07-12 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0009_alter_user_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userverification',
            options={'verbose_name': 'User Verification', 'verbose_name_plural': 'User Verification'},
        ),
        migrations.CreateModel(
            name='ResetPasswordVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_code', models.CharField(max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reset Password Verification',
                'verbose_name_plural': 'Reset Password Verification',
                'db_table': 'reset_password_verification',
            },
        ),
    ]