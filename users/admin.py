from django.contrib import admin
from django import forms
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    # def save_model(self, request, obj, form, change):
    #     if not obj.first_name:
    #         raise forms.ValidationError("First name needed......")
    #     if not obj.generalprofile.number:
    #         raise forms.ValidationError("number needed......")
    #     super().save_model(request, obj, form, change)
    # form = CustomUserForm
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "groups",
                    "first_name",
                    "last_name",
                    "email",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
    ordering = ("id",)
    list_filter = ("groups",)
    search_fields = ['username']

admin.site.register(CustomUser, CustomUserAdmin)

