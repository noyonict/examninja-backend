from django.db import models
from utils.base_model import BaseModel
from exam.models import Question, Exam, Subject
from user_management.models import User


class ExamHistory(BaseModel):
    name = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    exam_reference = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    total_marks = models.CharField(max_length=50)
    total_correct_answers = models.PositiveSmallIntegerField()
    total_number_unanswersed = models.PositiveSmallIntegerField()
    total_wrong_answers = models.PositiveSmallIntegerField()
    earned_points = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Exam Histories"


class FavoriteQuestion(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pinned_by = models.CharField(default="Manual", unique=True, max_length=15)

    class Meta:
        verbose_name_plural = "Favorite Questions"


class FavoriteExam(BaseModel):
    exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Favorit Exams"
