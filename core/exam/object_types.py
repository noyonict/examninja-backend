from graphene_django import DjangoObjectType
from exam.models import *

class ExamTitleType(DjangoObjectType):
    class Meta:
        model = ExamTitle
        fields = '__all__'

class SubjectCategoryType(DjangoObjectType):
    class Meta:
        model = SubjectCategory
        fields = '__all__'

class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject
        fields= '__all__'

class ChapterCategoryType(DjangoObjectType):
    class Meta:
        model = ChapterCategory
        fields = '__all__'

class ChapterType(DjangoObjectType):
    class Meta:
        model = Chapter
        fields = '__all__'

class BoardYearType(DjangoObjectType):
    class Meta:
        model = BoardYear
        fields = '__all__'

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionCommentType(DjangoObjectType):
    class Meta:
        model = QuestionComment
        fields = '__all__'

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionAnswerType(DjangoObjectType):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'

class QuestionPatternType(DjangoObjectType):
    class Meta:
        model = QuestionPattern
        fields = '__all__'

class ExamType(DjangoObjectType):
    class Meta:
        model = Exam
        fields = '__all__'