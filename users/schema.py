import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

class AuthMutation(graphene.ObjectType):
    delete_account = mutations.DeleteAccount.Field()
    password_change = mutations.PasswordChange.Field()
    refresh_token = mutations.RefreshToken.Field()
    register = mutations.Register.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    revoke_token = mutations.RevokeToken.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    verify_account = mutations.VerifyAccount.Field()
    verify_token = mutations.VerifyToken.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
