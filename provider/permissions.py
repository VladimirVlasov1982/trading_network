from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """
    Пользовательское разрешение, позволяющее только активным сотрудникам получать доступ к API
    """

    def has_permission(self, request, view):
        return request.user.is_active
