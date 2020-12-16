from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from authentication.serializers import UserSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        user_data = UserSerializer(instance=user, data=request.data)

        if not user_data.is_valid():
            return Response({'message': 'Invalid data'}, status=400)

        user_data.save()
        return Response(user_data.data)
