from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveDestroyAPIView
from .models import Question, Answer, User
from .serializers import AnswerSerializer, QuestionSerializer, UserSerializer, QuestionSearchSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from .permissions import IsQuestionAuthor, NoPermission
from django.contrib.postgres.search import SearchVector


class QuestionList(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        data = self.request.data
        if self.request.method == 'DELETE':
            permission_classes = [IsQuestionAuthor]
        elif self.request.method == "PATCH":
            if "favorited" in data:
                permission_classes = [IsAuthenticated]
            elif "title" in data or "body" in data:
                permission_classes = [NoPermission]
            elif "answered" in data:
                permission_classes = [IsQuestionAuthor]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.query_params.get("search"):
            return QuestionSearchSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        if self.request.query_params.get("search"):
            search_value = self.request.query_params.get("search")
            queryset = Question.objects.annotate(
                search=SearchVector("title", "body")
            ).filter(search=search_value)
            return queryset
        return super().get_queryset()


class AnswerList(ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        search_value = self.request.query_params.get("search")
        queryset = Question.objects.annotate(
            search=SearchVector("title", "body")
        ).filter(search=search_value)
        return queryset

    def get_permissions(self):
        if "search" not in self.request.query_params:
            permission_classes = [NoPermission]
        return [permission() for permission in permission_classes]


class UsersAnswerList(ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.filter(author_id=self.kwargs["pk"])
        return queryset

class QsAnswerList(ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Answer.objects.filter(question_id=self.kwargs["pk"])
        return queryset

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs["pk"])
        serializer.save(author=self.request.user, question=question)



class AnswerDetail(UpdateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Answer.objects.filter(question_id=self.kwargs["pk"])
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs["ans"])
        self.check_object_permissions(self.request, obj)
        return obj



class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
