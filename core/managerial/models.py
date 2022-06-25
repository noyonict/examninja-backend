from django.db import models
from utils.base_model import BaseModel


class PrivacyPolicy(BaseModel):
    title = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Privacy Policies"


FAQ_CHOICES = ((1, "NORMAL"), (2, "FEATURE"))


class FAQ(BaseModel):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    faq_type = models.CharField(max_length=10, choices=FAQ_CHOICES)

    class Meta:
        verbose_name_plural = "Frequently Asked Questions"
