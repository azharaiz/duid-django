from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Dompet
from .serializers import DompetSerializer


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class DompetView(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    permission_classes = (IsOwnerPermission,)
    serializer_class = DompetSerializer

    # Ensure a user sees only own Dompet objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Dompet.objects.filter(user=user)
        raise PermissionDenied()

    # Set user as owner of a Dompet object.
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValueError as error:
            raise PermissionDenied() from error
