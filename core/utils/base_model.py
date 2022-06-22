from django.db import models
from user_management.models import User


class BaseModel(models.Model):
    sequence = models.PositiveBigIntegerField()
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='created_by_user')
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='updated_by_user')

    class Meta:
        abstract = True
