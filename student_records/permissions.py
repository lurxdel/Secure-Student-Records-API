from rest_framework.permissions import BasePermission

class IsAdminOrFaculty(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.groups.filter(name__in=['Admin', 'Faculty']).exists())
