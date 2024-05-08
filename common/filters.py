from .models import Restaurant
import django_filters 
from django_filters import rest_framework as filters

class RestaurantFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name",lookup_expr="icontains")

    class Meta:
        model = Restaurant
        fields = ("name","id")