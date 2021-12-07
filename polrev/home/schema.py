import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Post

class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = []
        interfaces = (relay.Node, )

class Query(object):
    post = relay.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        summary = graphene.String()
        body = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, id, title, summary, body):
        print('mutate')
        print(id)
        # post = Post.query.get(id)
        post = graphene.Node.get_node_from_global_id(info, id)
        print(post)
        post.title = title
        post.summary = summary
        post.body = body
        post.save()
        ok = True

        return ok

class Mutation(graphene.ObjectType):
    update_post = UpdatePost.Field()
