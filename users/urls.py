from django.urls import path
from .views import UserRegistrationAPIView,UserLoginAPIView

urlpatterns = [
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]

