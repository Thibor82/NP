from rest_framework import viewsets
from .models import Post, Comment, Tag
from .serializers import PostSerializer, CommentSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import FilterSet, filters

class PostFilter(FilterSet):
    tag=filters.NumberFilter(field_name="tags__id")
    class Meta:
        model =Post
        fields =["tags"]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filterset_class = PostFilter
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     tag_id = self.request.query_params.get('tag')
    #     if tag_id:
    #        qs =qs.filter(tags__id=tag_id)
    #     return qs



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.request.query_params.get('post')
        if post_id:
            qs =qs.filter(post_id=post_id)
        return qs
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('-id')
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


