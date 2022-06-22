from django.db import models
from utils.base_model import BaseModel


class ExamTitle(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    expansion_of_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Exam Titles'
