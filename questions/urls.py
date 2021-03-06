"""questions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import SimpleRouter
from rest_framework import routers


router = SimpleRouter()
router.register(r'questions', views.QuestionList, basename='questions')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('questions/<int:pk>/answers/', views.QsAnswerList.as_view(), name="qs_answer_list"),
    path('questions/<int:pk>/answers/<int:ans>/', views.AnswerDetail.as_view(), name="answer_detail"),
    path('user/<int:pk>/answers/', views.UsersAnswerList.as_view(), name="users_answer_list"),
    path('user/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('answers/', views.AnswerList.as_view(), name="search_answer_list"),
    path('tags/', views.AddListTags.as_view(), name="add_list_tags"),
]
