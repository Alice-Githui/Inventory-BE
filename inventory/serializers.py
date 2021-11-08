from .models import *
from rest_framework import serializers

class AddNewInventory(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields="__all__"