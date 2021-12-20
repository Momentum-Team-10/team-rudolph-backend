from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        methods = ('DELETE', 'PATCH')
        if request.method in methods:
            if request.user.is_staff:
                return True
            return obj.author == request.user


class IsQuestionUnanswered(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if len(obj.answers.all()) == 0:
            return True
        return False


class NoPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False

    def has_permission(self, request, view):
        return False