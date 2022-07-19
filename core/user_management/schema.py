import graphql_jwt
import graphene
from user_management.input_types import *
from user_management.models import User, UserVerification, ResetPasswordVerification
import random
from utils.send_verification_sms import send_verification_sms, reset_password_verification_sms
from graphql import GraphQLError



class RegisterUser(graphene.Mutation):
    class Arguments:
        data = RegisterInput(required=True)

    message = graphene.String()

    def mutate(root, info, data):
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
            raise GraphQLError("Please enter correct credentials.")

        user.is_active = True
        user.is_phone_number_verified = True
        user.save()
        return {
            "message": "Your account has been activated."
        }


class ForgotPassword(graphene.Mutation):
    class Arguments:
        phone_number = graphene.String(required=True)
    message = graphene.String()
    def mutate(root, info, phone_number):
        user = User.objects.filter(phone_number=phone_number)
        if not user:
            raise GraphQLError("Phone number not registered.")
        verification_code = f'{random.randrange(1, 10**3):06}'
        ResetPasswordVerification.objects.create(
            user=user[0], verification_code=verification_code)
        reset_password_verification_sms(phone_number, verification_code)
        return {
            "message": "Reset password verification code has been sent to your phone number."
        }

class ResetPassword(graphene.Mutation):
    class Arguments:
        data = ResetPasswordInput(required=True)
    message = graphene.String()

    def mutate(root, info, data):
        user = User.objects.filter(phone_number=data['phone_number'])

        if not user:
            raise GraphQLError("Phone number not registered.")
        
        reset_password_verification = ResetPasswordVerification.objects.filter(user=user[0], verification_code=data['verification_code'])

        if not reset_password_verification:
            raise GraphQLError("Phone number or Verification Code is incorrect.")

        user = user[0]
        user.set_password(data['password'])
        user.save()
        
        return {
            "message": "Password has been reset."
        }



class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register_user = RegisterUser.Field()
    activate_user = ActivateUser.Field()
    forgot_password = ForgotPassword.Field()
    reset_password = ResetPassword.Field()


class Query(graphene.ObjectType):
    # resolve users
    pass


schema = graphene.Schema(mutation=Mutation)
