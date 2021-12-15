from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Question
from .serializers import QuestionSerializer

# Create your views here.

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
