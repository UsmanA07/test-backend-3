from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import Subscription


def make_payment(request):
    # TODO
    pass


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        # TODO
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        # TODO
        return Subscription.is_available == True


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
