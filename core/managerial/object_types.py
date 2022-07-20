from graphene_django import DjangoObjectType
from managerial.models import *


class PrivacyPolicyType(DjangoObjectType):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'

class FAQType(DjangoObjectType):
    class Meta:
        model = FAQ
        fields = '__all__'