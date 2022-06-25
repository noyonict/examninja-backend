from django.contrib import admin
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
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

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
    password_updated_at = models.DateTimeField()
    present_address = models.TextField()
    user_experience = models.PositiveIntegerField(default=0)
    user_marks = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(null=True, blank=True)
    last_active_at = models.DateTimeField()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        if self.nick_name:
            return self.nick_name.title()
        elif self.full_name:
            return self.full_name.title()
        else:
            return self.phone_number

    class Meta:
        db_table = 'user'
        verbose_name = "user"  # A human-readable name for the object
        verbose_name_plural = "users"  # The plural name for the object
        ordering = ('date_joined', )  # The default ordering for the object
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class PermissionAdmin(admin.ModelAdmin):

    class Meta:
        db_table = 'user_permission'
        verbose_name = "user_permission"  # A human-readable name for the object
        verbose_name_plural = "user_permissions"  # The plural name for the object
        # ordering = ('date_joined',)  # The default ordering for the object
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to
