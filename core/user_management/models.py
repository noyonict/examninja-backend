from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, phone_number,  password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone_number:
            raise ValueError('The given phone number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number=None,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(phone_number, password, **extra_fields)


GENDER_CHOICES = ((1, 'MALE'), (2, 'FEMALE'))


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    phone_number = models.CharField(
        max_length=15, unique=True, blank=False, null=False)
    is_phone_number_verified = models.BooleanField(default=False)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    password_updated_at = models.DateTimeField(auto_now=True)
    present_address = models.TextField()
    user_experience = models.PositiveIntegerField(default=0)
    user_marks = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(null=True, blank=True)
    last_login_time = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    def __str__(self):
        return self.phone_number
