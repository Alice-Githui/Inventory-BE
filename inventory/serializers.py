from .models import *
from rest_framework import serializers

class AddNewInventory(serializer.serializers):
    class Meta:
        model=Inventory
        fields=__all__