from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Question
from .serializers import QuestionSerializer

# Create your views here.

class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
