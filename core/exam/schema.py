import graphene
from exam.object_types import *
from exam.models import *
from utils.common import *
from graphql_jwt.decorators import login_required

class Query(graphene.ObjectType):
    exam_titles = graphene.List(ExamTitleType, pagination_input = PaginationInput())
    subject_catories = graphene.List(SubjectCategoryType, pagination_input = PaginationInput())
    subjects = graphene.List(SubjectType, pagination_input = PaginationInput())
    chapter_categories = graphene.List(ChapterCategoryType, pagination_input = PaginationInput())
    chapters = graphene.List(ChapterType, pagination_input = PaginationInput())
    board_years = graphene.List(BoardYearType, pagination_input = PaginationInput())
    questions = graphene.List(QuestionType, pagination_input = PaginationInput())
    question_comments = graphene.List(QuestionCommentType, pagination_input = PaginationInput())
    answers = graphene.List(AnswerType, pagination_input = PaginationInput())
    question_answers = graphene.List(QuestionAnswerType, pagination_input = PaginationInput())
    question_patterns = graphene.List(QuestionPatternType, pagination_input = PaginationInput())
    exams = graphene.List(ExamType, pagination_input = PaginationInput())

    @login_required
    def resolve_exam_titles(root, info, pagination_input, **kwargs):
        return ExamTitle.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_subject_categories(root, info, pagination_input, **kwargs):
        return SubjectCategory.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]

    @login_required
    def resolve_subjects(root, info, pagination_input, **kwargs):
        return Subject.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_chapter_categories(root, info, pagination_input, **kwargs):
        return ChapterCategory.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_board_years(root, info, pagination_input, **kwargs):
        return BoardYear.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]

    @login_required
    def resolve_questions(root, info, pagination_input, **kwargs):
        return Question.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_question_comments(root, info, pagination_input, **kwargs):
        return QuestionComment.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_answers(root, info, pagination_input, **kwargs):
        return Answer.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_question_answers(root, info, pagination_input, **kwargs):
        return QuestionAnswer.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]

    @login_required
    def resolve_question_patters(root, info, pagination_input, **kwargs):
        return QuestionPattern.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]

    @login_required
    def resolve_exams(root, info, pagination_input, **kwargs):
        return Exam.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    

