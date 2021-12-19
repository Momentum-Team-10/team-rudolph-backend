from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveDestroyAPIView
from .models import Question, Answer, User, Tag
from .serializers import AnswerSerializer, QuestionSerializer, UserSerializer, QuestionSearchSerializer, TagSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly 
from .permissions import IsQuestionAuthor, NoPermission
from django.contrib.postgres.search import SearchVector

class AddListTags(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class QuestionList(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        if 'favorited' in self.request.data:
            question = self.get_object()
            data_copy = self.request.data.copy()
            user = self.request.user.pk
            data_copy['favorited'] = question.update_favs(user)
            kwargs['data'] = data_copy
        return serializer_class(*args, **kwargs)

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
        queryset = Answer.objects.annotate(
            search=SearchVector("body")
        ).filter(search=search_value)
        return queryset

    def get_permissions(self):
        if "search" not in self.request.query_params:
            permission_classes = [NoPermission]
        else:
            permission_classes = [AllowAny]
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

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        if 'favorited' in self.request.data:
            answer = self.get_object()
            data_copy = self.request.data.copy()
            user = self.request.user.pk
            data_copy['favorited'] = answer.update_favs(user)
            kwargs['data'] = data_copy
        return serializer_class(*args, **kwargs)


class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


