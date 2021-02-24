from rest_framework import permissions

from .models import RoleUser


class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.is_staff
                     or request.user.role == RoleUser.ADMIN))
