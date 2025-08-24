
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Rating
from .serializers import RatingSerializer

@swagger_auto_schema(tags=['Ratings'])
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.validated_data['post']
        if post.author.user == request.user:
            return Response({'detail': 'You cannot rate your own post.'}, status=status.HTTP_403_FORBIDDEN)
        if Rating.objects.filter(post=post, user=request.user).exists():
            return Response({'detail': 'You have already rated this post.'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)