import graphene
from exam.object_types import *
from exam.models import *

class Query(graphene.ObjectType):
    exam_titles = graphene.List(ExamTitleType)
    subject_catories = graphene.List(SubjectCategoryType)
    subjects = graphene.List(SubjectType)
    chapter_categories = graphene.List(ChapterCategoryType)
    chapters = graphene.List(ChapterType)
    board_years = graphene.List(BoardYearType)
    questions = graphene.List(QuestionType)
    question_comments = graphene.List(QuestionCommentType)
    answers = graphene.List(AnswerType)
    question_answers = graphene.List(QuestionAnswerType)
    question_patterns = graphene.List(QuestionPatternType)
    exams = graphene.List(ExamType)

    
    def resolve_exam_titles(root, info, **kwargs):
        return ExamTitle.objects.all()
    def resolve_subject_categories(root, info, **kwargs):
        return SubjectCategory.objects.all()
    def resolve_subjects(root, info, **kwargs):
        return Subject.objects.all()
    def resolve_chapter_categories(root, info, **kwargs):
        return ChapterCategory.objects.all()
    def resolve_board_years(root, info, **kwargs):
        return BoardYear.objects.all()
    def resolve_questions(root, info, **kwargs):
        return Question.objects.all()
    def resolve_question_comments(root, info, **kwargs):
        return QuestionComment.objects.all()
    def resolve_answers(root, info, **kwargs):
        return Answer.objects.all()
    def resolve_question_answers(root, info, **kwargs):
        return QuestionAnswer.objects.all()
    def resolve_question_patters(root, info, **kwargs):
        return QuestionPattern.objects.all()
    def resolve_exams(root, info, **kwargs):
        return Exam.objects.all()
    

