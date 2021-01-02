from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied

from target.models import Target
from target.serializers import TargetSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class TargetView(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    permission_classes = (IsOwner,)
    serializer_class = TargetSerializer

    # Ensure a user sees only own Dompet objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Target.objects.filter(user=user)
        raise PermissionDenied()

    # Set user as owner of a Dompet object.
    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValueError as value_error:
            raise PermissionDenied() from value_error
