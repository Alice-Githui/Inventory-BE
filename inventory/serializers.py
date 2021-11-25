from .models import *
from rest_framework import serializers

class RegisterNewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        extra_kwargs = {"password": {'write_only': True}}

    def create(self, validated_data):
            password =validated_data.pop('password', None)
            instance =self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            # instance.is_customer=True  
            # instance.is_active=False
            instance.save()   
            return instance

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