from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from django.db.models.constraints import UniqueConstraint



# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name')

    def __repr__(self):
        return f"<Tag name={self.name}>"

    def __str__(self):
        return self.name

class User(AbstractUser):
    image_url = models.CharField(max_length=250, blank=True, null=True)
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
    upvotes = models.ManyToManyField('User', related_name="upvoted_questions", blank=True)
    downvotes = models.ManyToManyField('User', related_name="downvoted_questions", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited = models.ManyToManyField('User', related_name="fav_questions", blank=True)
    answered = models.ForeignKey('Answer', on_delete=models.DO_NOTHING, related_name="accepted", null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name="questions_tag", blank=True)

    class Meta:
            ordering = ('votes', 'created_at')


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

    def update_favs(self, id):
        fav_users = self.get_fav_users()
        if id in fav_users:
            fav_users.remove(id)
        else:
            fav_users.append(id)
        return fav_users

    def update_votes(self, action, id):
        if action == 'upvote':
            upvotes, downvotes = self.upvote(id)
        elif action == 'downvote':
            upvotes, downvotes = self.downvote(id)
        votes = len(upvotes)-len(downvotes)
        return upvotes, downvotes, votes

    def get_votes(self):
        upvotes = self.convert_to_pk(list(self.upvotes.all()))
        downvotes = self.convert_to_pk(list(self.downvotes.all()))
        return upvotes, downvotes

    def convert_to_pk(self, list):
        new_list = []
        for user in list:
            new_list.append(user.pk)
        return new_list

    def upvote(self, id):
        upvotes, downvotes = self.get_votes()
        if id in upvotes:
            upvotes.remove(id)
        else:
            upvotes.append(id)
            if id in downvotes:
                downvotes.remove(id)
        return upvotes, downvotes

    def downvote(self, id):
        upvotes, downvotes = self.get_votes()
        if id in downvotes:
            downvotes.remove(id)
        else:
            downvotes.append(id)
            if id in upvotes:
                upvotes.remove(id)
        return upvotes, downvotes


class Answer(models.Model):
    body = models.TextField()
    author = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name="answers")
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="answers")
    votes = models.IntegerField(default=0)
    upvotes = models.ManyToManyField('User', related_name="upvoted_answers", blank=True)
    downvotes = models.ManyToManyField('User', related_name="downvoted_answers", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited = models.ManyToManyField('User', related_name="fav_answers", blank=True)

    class Meta:
        ordering = ('votes', 'created_at')




    def __repr__(self):
        return f"<Answer author={self.author} question={self.question}>"

    def __str__(self):
        return self.title

    def get_fav_users(self):
        favs = self.favorited.all()
        fav_users = []
        for user in favs:
            fav_users.append(user.pk)
        return fav_users

    def update_favs(self, id):
        fav_users = self.get_fav_users()
        if id in fav_users:
            fav_users.remove(id)
        else:
            fav_users.append(id)
        return fav_users

    def update_votes(self, action, id):
        if action == 'upvote':
            upvotes, downvotes = self.upvote(id)
        elif action == 'downvote':
            upvotes, downvotes = self.downvote(id)
        votes = len(upvotes)-len(downvotes)
        return upvotes, downvotes, votes

    def get_votes(self):
        upvotes = self.convert_to_pk(list(self.upvotes.all()))
        downvotes = self.convert_to_pk(list(self.downvotes.all()))
        return upvotes, downvotes

    def convert_to_pk(self, list):
        new_list = []
        for user in list:
            new_list.append(user.pk)
        return new_list

    def upvote(self, id):
        upvotes, downvotes = self.get_votes()
        if id in upvotes:
            upvotes.remove(id)
        else:
            upvotes.append(id)
            if id in downvotes:
                downvotes.remove(id)
        return upvotes, downvotes

    def downvote(self, id):
        upvotes, downvotes = self.get_votes()
        if id in downvotes:
            downvotes.remove(id)
        else:
            downvotes.append(id)
            if id in upvotes:
                upvotes.remove(id)
        return upvotes, downvotes

