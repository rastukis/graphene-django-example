from graphene import Node, ObjectType

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.posts.models import Post

class PostNode(DjangoObjectType):

    class Meta:
        model = Post
        only_fields = ('title', 'content')
        # Para excluir se puede usar
        # exclude_fields = ('published', 'owner')
        interfaces = (Node, )

class QueryPost(ObjectType):
    all_posts = DjangoFilterConnectionField(PostNode)

    def resolver_all_posts(self, info, **kwargs):
        return Post.objects.filter(published=True)

    # Filtro de Posts basado en el usuario
    my_posts = DjangoFilterConnectionField(PostNode)

    def resolve_my_posts(self, info):
        if not info.context.user.is_authenticated():
            return Post.objects.none()
        else:
            return Post.objects.filter(owner=info.context.user)