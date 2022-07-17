import graphene
from managerial.object_types import *
from managerial.models import *


class Query(graphene.ObjectType):
    privacy_policies = graphene.List(PrivacyPolicyType)
    faq = graphene.List(FAQType)

    def resolve_privacy_policies(root, info, **kwargs):
        return PrivacyPolicy.objects.all()
    
    def resolve_faq(root, info, **kwargs):
        return FAQ.objects.all()