from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        user_data = UserSerializer(data=request.data)

        if not user_data.is_valid():
            return Response({'message': 'Invalid data'}, status=400)

        user_data.save()
        return Response(user_data.data)
