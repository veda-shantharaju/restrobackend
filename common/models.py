from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

    
class Restaurant(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    