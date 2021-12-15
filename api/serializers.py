from rest_framework import serializers
from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
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
        