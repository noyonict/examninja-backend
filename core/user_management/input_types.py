from graphene import InputObjectType
import graphene


class RegisterInput(InputObjectType):
    phone_number = graphene.String(required=True)
    password = graphene.String(required=True)


class VerificationInput(InputObjectType):
    phone_number = graphene.String(required=True)
    verification_code = graphene.String(required=True)

class ResetPasswordInput(InputObjectType):
    phone_number = graphene.String(required=True)
    verification_code = graphene.String(required=True)
    password = graphene.String(required=True)
