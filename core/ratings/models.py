
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from blog.models import Post

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    class Meta:
        unique_together = ('post', 'user')
    def __str__(self):
        return f'{self.score}/5 by {self.user.email} for {self.post.title}'