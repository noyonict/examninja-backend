import graphene
from managerial.object_types import *
from managerial.models import *
from utils.common import *
from graphql_jwt.decorators import login_required


class Query(graphene.ObjectType):
    privacy_policies = graphene.List(PrivacyPolicyType, input=PaginationInput())
    faq = graphene.List(FAQType, pagination_input=PaginationInput())

    @login_required
    def resolve_privacy_policies(root, info, pagination_input, **kwargs):
        print(pagination_input)
        return PrivacyPolicy.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]
    
    @login_required
    def resolve_faq(root, info, pagination_input, **kwargs):
        print(pagination_input)
        return FAQ.objects.filter(**default_filter)[pagination_input['offset']:pagination_input['offset']]