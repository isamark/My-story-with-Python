from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 读权限被允许所有人，包括GET, HRAD, OPTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 写的权限被允许
        return obj.operator == request.user