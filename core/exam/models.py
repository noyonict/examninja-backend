from django.db import models
from utils.base_model import BaseModel
from user_management.models import User


class ExamTitle(BaseModel):
    name = models.CharField(
        max_length=50, help_text='Name of the topic. (Ex: SSC)', unique=True)
    expansion_of_name = models.CharField(max_length=150, blank=True, null=True,
                                         help_text='Expansion of the name, if any.  (Ex: Secondary School Certificate')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'exam_title'
        verbose_name = "Exam Title"  # A human-readable name for the object
        verbose_name_plural = "1. Exam Titles"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class SubjectCategory(BaseModel):
    name = models.CharField(
        max_length=50, help_text='Name of the Subject Category. (Ex: Science/Arts/Commerce)',)
    exam_title = models.ForeignKey(ExamTitle, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject_category'
        verbose_name = "Subject Category"  # A human-readable name for the object
        verbose_name_plural = "2.1. Subject Categories"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class Subject(BaseModel):
    name = models.CharField(
        max_length=150, help_text='Name of the subject. (Ex: Bangla First Paper)')
    code = models.CharField(max_length=50, null=True, blank=True)
    subject_category = models.ForeignKey(
        SubjectCategory,  on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'
        verbose_name = "Subject"  # A human-readable name for the object
        verbose_name_plural = "2.2. Subjects"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class ChapterCategory(BaseModel):
    name = models.CharField(
        max_length=50, help_text='Name of the subject category. (Ex: Goddo/Poddo/Uponnas/Natok)')
    number_of_question = models.PositiveIntegerField(
        blank=True, null=True, help_text='Total Number of question are stored in the databse under this catagory')
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'chapter_category'
        verbose_name = "Chapter Category"  # A human-readable name for the object
        verbose_name_plural = "3.1. Chapter Categories"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class Chapter(BaseModel):
    name = models.CharField(
        max_length=150, help_text='Name of the chapter. (Ex: বই পড়া)')
    chapter_position = models.PositiveIntegerField(
        blank=True, null=True, help_text='What is the position of this chapter.')
    chapter_category = models.ForeignKey(
        ChapterCategory, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'chapter'
        verbose_name = "Chapter"  # A human-readable name for the object
        verbose_name_plural = "3.2. Chapters"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class BoardYear(BaseModel):
    board_name = models.CharField(
        max_length=255, help_text='Name of the Board With year. (Ex: Rajshahi)')
    year = models.CharField(
        max_length=4, help_text='Year (Ex: 2018) ', null=True, blank=True)
    code = models.CharField(
        max_length=10, help_text='Short Code of the Board. (Ex: Raj-18)', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.code:
            if self.year:
                self.code = f"{self.board_name[0:3]}-{self.year[-2:]}"
            else:
                self.code = f"{self.board_name[0:3]}"
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'board_year'
        verbose_name = "Board"  # A human-readable name for the object
        verbose_name_plural = "4. Boards"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'code', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class Question(BaseModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)
    uddipok = models.TextField()
    question = models.TextField()
    image = models.ImageField(upload_to="media/question/images/")
    hints = models.TextField()
    boards = models.ManyToManyField(BoardYear)

    class Meta:
        db_table = 'question'
        verbose_name = "Question"  # A human-readable name for the object
        verbose_name_plural = "5.1. Questions"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class QuestionComment(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'question_comment'
        verbose_name = "Question Comment"  # A human-readable name for the object
        verbose_name_plural = "5.2. Question Comment"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class Answer(BaseModel):
    value = models.TextField()

    class Meta:
        db_table = 'answere'
        verbose_name = "Answere"  # A human-readable name for the object
        verbose_name_plural = "6.1. Answeres"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class QuestionAnswer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Answer, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'question_answer'
        verbose_name = "Question Answer"  # A human-readable name for the object
        verbose_name_plural = "6.2. Question Answers"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class QuestionPattern(BaseModel):
    name = models.CharField(max_length=150)
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)
    number_of_questions = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'question_pattern'
        verbose_name = "Question Pattern"  # A human-readable name for the object
        verbose_name_plural = "6.3. Question Patterns"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to


class Exam(BaseModel):
    name = models.CharField(max_length=150)
    exam_title = models.ForeignKey(ExamTitle, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    question_patterns = models.ManyToManyField(QuestionPattern)
    number_of_questions = models.PositiveSmallIntegerField()
    exam_cost = models.FloatField()
    exam_procedure = models.TextField()

    class Meta:
        db_table = 'exam'
        verbose_name = "Exam"  # A human-readable name for the object
        verbose_name_plural = "7. Exams"  # The plural name for the object
        # The default ordering for the object
        ordering = ('sequence', 'created_at')
        # default_permissions = ('add', 'change', 'view')
        # permissions = [('can_create_topic', 'Can create topic')]
        # order_with_respect_to = 'question'  # Makes this object orderable with respect to the given field,
        # # usually a ForeignKey
        # unique_together = [['driver', 'restaurant']]
        # app_label = 'myapp'  # If a model is defined outside of an application in INSTALLED_APPS, it must declare
        # # which app it belongs to
