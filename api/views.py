from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from .models import Question, Answer
from .serializers import AnswerSerializer, QuestionSerializer

# Create your views here.

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionDetail(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    
class UsersAnswerList(ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.filter(author_id=self.kwargs["pk"])
        return queryset

class QsAnwerList(ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.filter(question_id=self.kwargs["pk"])
        return queryset


class AnswerDetail(UpdateAPIView):
    serializer_class = AnswerSerializer


    def get_queryset(self):
        queryset = Answer.objects.filter(question_id=self.kwargs["pk"])
        return queryset
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs["ans"])
        self.check_object_permissions(self.request, obj)
        return obj
