from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, serializers, status

class UserRegistrationAPIView(APIView):
    def validate(self, data):
        if not data.get("email"):
            raise serializers.ValidationError({'message': 'Email is needed...!!!'})
        if CustomUser.objects.filter(email__iexact=data.get("email")).exists():
            raise serializers.ValidationError({'message': 'Email already exists. Please try to login...!!!'})
        return True
    def post(self, request):
        if self.validate(request.data):
            CustomUser.objects.create(
                username=request.data.get("username"),
                email=request.data.get("email"),
                password=request.data.get("password"),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name")
            )
            return Response(
                {
                    "message": "signup successfull",
                }, status=status.HTTP_201_CREATED
            )
        return Response(
                    {
                        "message":"unsuccessfully"
                    }, status=status.HTTP_400_BAD_REQUEST
                )

class UserLoginAPIView(KnoxLoginView):
    # permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        response = super(UserLoginAPIView, self).post(request, format=None)
        response.data["id"] = user.id
        response.data["name"] = f"{user.first_name} {user.last_name}"
        return response