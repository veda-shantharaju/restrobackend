from django.shortcuts import render
from .models import Restaurant
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, serializers, status
from rest_framework.permissions import IsAuthenticated
from .serializers import RestaurantSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from .filters import RestaurantFilter
# Create your views here.
class AddRestroAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def validate(self, data):
        if not data.get("phone"):
            raise serializers.ValidationError({'message': 'number is needed...!!!'})
        if Restaurant.objects.filter(phone=data.get("phone")).exists():
            raise serializers.ValidationError({'message': 'number already exists'})
        return True
    def post(self, request):
        if self.validate(request.data):
            Restaurant.objects.create(
                name=request.data.get("name"),
                address=request.data.get("address"),
                phone=request.data.get("phone")
            )
            return Response(
                {
                    "message": "Restaurant added successfull",
                }, status=status.HTTP_201_CREATED
            )
        return Response(
                    {
                        "message":"unsuccessfully"
                    }, status=status.HTTP_400_BAD_REQUEST
                )

class RestroList(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all().order_by("id")
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilter

class UpdateRestroAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def validate(self, data):
        if not Restaurant.objects.filter(id = self.request.query_params["id"]).exists():
            raise serializers.ValidationError({'message': 'id doesnt exists'})
        return True
    def post(self, request, *args, **kwargs):
        if self.validate(request.data):
            query = Restaurant.objects.filter(id = self.request.query_params["id"])
            query.update(
                name=request.data.get("name"),
                address=request.data.get("address"),
                phone=request.data.get("phone")
            )
        return Response(
                {
                    "message": "updated successfully"
                }, status=status.HTTP_200_OK
            )

class DeleteRestroAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def validate(self, data):
        if not Restaurant.objects.filter(id = self.request.query_params["id"]).exists():
            raise serializers.ValidationError({'message': 'id doesnt exists'})
        return True
    def delete(self, request, *args, **kwargs):
        if self.validate(request.data):
            query = Restaurant.objects.filter(id = self.request.query_params["id"])
            query.delete()
        return Response(
                {
                    "message": "deleted successfully"
                }, status=status.HTTP_200_OK
            )