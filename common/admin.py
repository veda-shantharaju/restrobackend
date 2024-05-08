from django.contrib import admin
from common.models import Restaurant

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Restaurant._meta.fields]
    date_hierarchy = "created"

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # form.base_fields["author"].initial = request.user
        return form
    
admin.site.register(Restaurant,RestaurantAdmin)
