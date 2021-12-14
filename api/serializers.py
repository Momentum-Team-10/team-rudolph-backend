from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Question
        fields = (
            'title',
            'body',
            'author',
            'votes',
            'created_at',
            'favorited',
            'answer',
        )