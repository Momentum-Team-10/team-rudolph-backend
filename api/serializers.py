from rest_framework import serializers
from .models import Answer, Question, User, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'pk',
            'name',
            'slug',
        )

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Answer 
        fields = (
            'pk',
            'body',
            'author',
            'question',
            'votes',
            'upvotes',
            'downvotes',
            'created_at',
            'favorited',
        )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    tags = serializers.SlugRelatedField(read_only=True, many=True, slug_field="tag")

    class Meta:
        model = Question
        fields = (
            'pk',
            'title',
            'body',
            'author',
            'votes',
            'upvotes',
            'downvotes',
            'answers',
            'created_at',
            'favorited',
            'answered',
            'tags',
        )


class QuestionForUserSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tags = serializers.SlugRelatedField(read_only=True, many=True, slug_field="tag")

    class Meta:
        model = Question
        fields = (
            'pk',
            'title',
            'body',
            'author',
            'votes',
            'created_at',
            'favorited',
            'answered',
            'tags',
        )


class QuestionSearchSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tags = serializers.SlugRelatedField(read_only=True, many=True, slug_field="tag")

    class Meta:
        model = Question
        fields = (
            'pk',
            'title',
            'body',
            'author',
            'votes',
            'created_at',
            'favorited',
            'answered',
            'tags',
        )


class UserSerializer(serializers.ModelSerializer):
    questions = QuestionForUserSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'bio',
            'questions',
            'answers',
            'image_url',
            'date_joined',
        )


