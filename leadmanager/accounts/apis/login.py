from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from knox.models import AuthToken

from ..serializers import UserSerializer, LoginSerializer


class LoginAPI(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        user_data = UserSerializer(user, 
                context=self.get_serializer_context()).data

        return Response({
            "user": user_data,
            "token": token
        })
