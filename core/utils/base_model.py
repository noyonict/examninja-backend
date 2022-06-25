from django.db import models
from user_management.models import User


class BaseModel(models.Model):
    sequence = models.PositiveBigIntegerField(default=0, help_text='Ordering Criteria.')
    is_published = models.BooleanField(default=False, help_text='If false, it will be unavailable for end user!')
    is_active = models.BooleanField(default=False, help_text='Toggles the global visibility of the record, if flase then it will be deleted for the user')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='%(app_label)s_%(class)s_created_by', db_index=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='%(app_label)s_%(class)s_updated_by', db_index=False)

    class Meta:
        abstract = True
