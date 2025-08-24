
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = Rating
        fields = ['id', 'post', 'user', 'user_email', 'score']
        read_only_fields = ['user']