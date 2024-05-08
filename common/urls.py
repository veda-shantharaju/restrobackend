from django.urls import path
from .views import AddRestroAPIView,RestroList,UpdateRestroAPIView,DeleteRestroAPIView
urlpatterns = [
    path('addrestro/', AddRestroAPIView.as_view(), name='add'),
    path('restrolist/', RestroList.as_view(), name='list'),
    path('updaterestro/', UpdateRestroAPIView.as_view(), name='update'),
    path('deleterestro/', DeleteRestroAPIView.as_view(), name='delete'),

]