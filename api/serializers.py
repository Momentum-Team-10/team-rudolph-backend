from rest_framework import serializers
from .models import Answer, Question, User


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
            'created_at',
            'favorited',
        )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Question
        fields = (
            'pk',
            'title',
            'body',
            'author',
            'votes',
            'answers',
            'created_at',
            'favorited',
            'answered',
        )


class QuestionForUserSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
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
        )


class UserSerializer(serializers.ModelSerializer):
    questions = QuestionForUserSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'username',
            'bio',
            'questions',
            'answers',
            'image_url',
        )