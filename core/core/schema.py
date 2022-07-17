import graphene
from user_management.schema import Mutation as AuthMutation
from exam.schema import Query as ExamQuery
from exam_history.schema import Query as ExamHistoryQuery
from managerial.schema import Query as ManagerialQuery

class Query(ExamQuery, ExamHistoryQuery, ManagerialQuery):
    pass

class Mutation(AuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
