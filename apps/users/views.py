from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.users.models import CustomUser
from apps.users.serializers import RegistrationSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = serializer.validated_data['token']
        return Response({
            'email': user.email,
            'token': token
        })
