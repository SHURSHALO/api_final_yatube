from rest_framework import permissions


class OnlyAuthorHasPerm(permissions.BasePermission):
    '''Кастомное разрешение, разрешает доступ только автору объекта.'''

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    '''Кастомное разрешение, только для чтения для безопасных методов.'''
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
