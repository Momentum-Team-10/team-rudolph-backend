from rest_framework import permissions


class IsQuestionAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            if request.user.is_staff:
                return True
            return obj.author == request.user


class NoPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False

    def has_permission(self, request, view):
        return False