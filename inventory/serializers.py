from .models import *
from rest_framework import serializers

class AddNewInventory(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields="__all__"

class UpdateStoreInventory(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields = ["quantity"]

class SellStoreInventory(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields=["quantity"]