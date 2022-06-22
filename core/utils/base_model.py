from django.db import models
from user_management.models import User


class BaseModel(models.Model):
    sequence = models.PositiveBigIntegerField()
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='%(app_label)s_%(class)s_created_by')
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='%(app_label)s_%(class)s_updated_by')

    class Meta:
        abstract = True
