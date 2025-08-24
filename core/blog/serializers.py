from rest_framework import serializers
from django.db.models import Avg
from .models import Post, Category
from comments.serializers import CommentSerializer
from accounts.serializers import ProfileSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    comments = CommentSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image', 'author', 'category',
            'created_at', 'updated_at', 'comments', 'average_rating'
        ]
        read_only_fields = ['author']

    def get_average_rating(self, obj):
        avg = obj.ratings.aggregate(Avg('score'))['score__avg']
        return round(avg, 2) if avg else None

    def to_representation(self, instance):
        """
        Customize the API output for read operations.
        """

        representation = super().to_representation(instance)
        if instance.category:
            representation['category'] = CategorySerializer(instance.category).data
        
        return representation