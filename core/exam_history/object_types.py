from graphene_django import DjangoObjectType
from exam_history.models import *

class ExamHistoryType(DjangoObjectType):
    class Meta:
        model = ExamHistory
        fields = '__all__'

class FavoriteQuestionType(DjangoObjectType):
    class Meta:
        model = FavoriteQuestion
        fields = '__all__'

class FavoriteExamType(DjangoObjectType):
    class Meta:
        model = FavoriteExam
        fields = '__all__'