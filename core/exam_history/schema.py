import graphene
from exam_history.models import *
from exam_history.object_types import *
from utils.common import *
from graphql_jwt.decorators import login_required

class Query(graphene.ObjectType):
    exam_histories = graphene.List(ExamHistoryType, pagination_input = PaginationInput())
    favorite_questions = graphene.List(FavoriteQuestionType, pagination_input = PaginationInput())
    favorite_exams = graphene.List(FavoriteExamType, pagination_input = PaginationInput())

    @login_required
    def resolve_exam_histories(root, info, pagination_input, **kwargs):
        return ExamHistory.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_favorite_questions(root, info, pagination_input, **kwargs):
        return FavoriteQuestion.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_favorite_exams(root, info, pagination_input, **kwargs):
        return FavoriteExam.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]