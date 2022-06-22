from django.db import models
from utils.base_model import BaseModel


class ExamTitle(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    expansion_of_name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Exam Titles'


class SubjectCategory(BaseModel):
    name = models.CharField(max_length=50)
    exam_title = models.ForeignKey(ExamTitle, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subject Categories"


class Subject(BaseModel):
    name = models.CharField(max_length=150, )
    code = models.CharField(max_length=50, null=True, blank=True)
    subject_category = models.ForeignKey(
        SubjectCategory,  on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subjects"


class ChapterCategory(BaseModel):
    name = models.CharField(max_length=50)
    number_of_question = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Chapter Categories"


class Chapter(BaseModel):
    name = models.CharField(max_length=150)
    chapter_position = models.PositiveIntegerField()
    chapter_category = models.ForeignKey(
        ChapterCategory, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Chapters"


# class BoardYear(BaseModel):
#     name = models.CharField(max_length=150)
#     year = models.CharField(max_length=4, null=True, blank=True)
#     code = models.CharField(max_length=10, null=True, blank=True)
