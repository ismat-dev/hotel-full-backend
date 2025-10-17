from django.shortcuts import render
from .serializers import RegitserSerializer, LoginSerializer, UsersSerializer
from . permissions import IsAdmin
from .models import UserProfile
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListUsers(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegitserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class Exit(APIView):
    def post(self, request):
        try:
            request.user.authtoken.delete()
            return Response({'Message': 'Succesfully logged out'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        