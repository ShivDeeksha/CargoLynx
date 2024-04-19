from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
class UserRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        # Set is_verified based on your logic
        user.is_verified = False  # Example logic, modify as needed
        user.save()


from django.urls import reverse

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active and user.is_verified:
                    refresh = RefreshToken.for_user(user)
                    response_data = {
                        'message': 'Login successful',
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    error_message = 'User account is not active or verified'
                    return Response({'error': error_message}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                error_message = 'Invalid username or password'
                return Response({'error': error_message}, status=status.HTTP_401_UNAUTHORIZED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

