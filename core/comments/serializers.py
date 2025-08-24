
from rest_framework import serializers
from .models import Comment
from accounts.serializers import ProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['author']