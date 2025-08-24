
from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsOwnerOrReadOnly

@swagger_auto_schema(tags=['Comments'])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
