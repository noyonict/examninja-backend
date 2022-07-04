import graphql_jwt
import graphene
from user_management.input_types import *
from user_management.models import User, UserVerification, UserManager
import random
from utils.send_verification_sms import send_verification_sms


class RegisterUser(graphene.Mutation):
    class Arguments:
        data = RegisterInput(required=True)

    message = graphene.String()

    def mutate(root, info, data):
        user_manager = UserManager()
        user = User(phone_number=data['phone_number'])
        user.set_password(data['password'])
        user.is_active = False
        user.save()
        verification_code = f'{random.randrange(1, 10**3):06}'
        UserVerification.objects.create(
            user=user, verification_code=verification_code)
        send_verification_sms(data['phone_number'], verification_code)
        return {
            "message": f"A verification code has been sent to {data['phone_number']}."
        }


class ActivateUser(graphene.Mutation):
    class Arguments:
        data = VerificationInput(required=True)
    message = graphene.String()

    def mutate(root, info, data):
        user = User.objects.get(phone_number=data['phone_number'])
        verification_code = UserVerification.objects.filter(
            user=user, verification_code=data['verification_code'])

        if not verification_code:
            return {
                "message": "Please enter valid verification code."
            }

        user.is_active = True
        user.is_phone_number_verified = True
        user.save()
        return {
            "message": "Your account has been activated."
        }


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register_user = RegisterUser.Field()
    activate_user = ActivateUser.Field()


class Query(graphene.ObjectType):
    # resolve users
    pass


schema = graphene.Schema(mutation=Mutation)
