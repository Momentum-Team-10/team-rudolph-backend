from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    image_url = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Question(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name="questions")
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited = models.ManyToManyField('User', related_name="fav_questions", blank=True)
    answered = models.BooleanField(default=False)

class Answer(models.Model):
    body = models.TextField()
    author = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name="answers")
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="answers")
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited = models.ManyToManyField('User', related_name="fav_answers", blank=True)
