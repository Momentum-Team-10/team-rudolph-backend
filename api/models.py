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
    voted_on = models.ManyToManyField('User', related_name="voted_questions", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited = models.ManyToManyField('User', related_name="fav_questions", blank=True)
    answered = models.ForeignKey('Answer', on_delete=models.DO_NOTHING, related_name="accepted", null=True, blank=True)


    def __repr__(self):
        return f"<Question title={self.title}>"

    def __str__(self):
        return self.title

    def get_fav_users(self):
        favs = self.favorited.all()
        fav_users = []
        for user in favs:
            fav_users.append(user.pk)
        return fav_users

    def update_favs(self, request):
        fav_users = self.get_fav_users()
        user = request.data["favorited"][0]
        if user in fav_users:
            new_favs = fav_users.remove(user)
        else:
            new_favs = fav_users.append(user)
            new_favs.sort()
        return new_favs

class Answer(models.Model):
    body = models.TextField()
    author = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name="answers")
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="answers")
    votes = models.IntegerField(default=0)
    voted_on = models.ManyToManyField('User', related_name="voted_answers", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited = models.ManyToManyField('User', related_name="fav_answers", blank=True)

    def __repr__(self):
        return f"<Answer author={self.author} question={self.question}>"

    def __str__(self):
        return self.title
