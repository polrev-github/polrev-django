import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = []
        interfaces = (relay.Node, )

class Query(object):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, id, username, email):
        print('mutate')
        print(id)
        user = graphene.Node.get_node_from_global_id(info, id)
        print(user)
        user.username = username
        user.email = email
        user.save()
        ok = True

        return ok

class Mutation(graphene.ObjectType):
    update_user = UpdateUser.Field()
