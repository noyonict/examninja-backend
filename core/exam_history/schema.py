import graphene
from exam_history.models import *
from exam_history.object_types import *

class Query(graphene.ObjectType):
    exam_histories = graphene.List(ExamHistoryType)
    favorite_questions = graphene.List(FavoriteQuestionType)
    favorite_exams = graphene.List(FavoriteExamType)

    def resolve_exam_histories(root, info, **kwargs):
        return ExamHistory.objects.all()
    
    def resolve_favorite_questions(root, info, **kwargs):
        return FavoriteQuestion.objects.all()
    
    def resolve_favorite_exams(root, info, **kwargs):
        return FavoriteExam.objects.all()