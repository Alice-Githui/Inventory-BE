from django.shortcuts import render
# from rest_framework.views import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import serializers,status
from django.core.checks import messages
from .serializers import *

# Create your views here.
class AddStoreInventory(generics.CreateAPIView):
    serializer_class=AddNewInventory

    def post(self, request, *args, **kwargs):
        # item_id=self.kwargs["pk"]
        # print(item_id)

        serializer=self.serializer_class(data=request.data)

        # item=Inventory.objects.get(pk=item_id)
        # item_quantity=item.quantity
        # print(item_quantity)

        # quantity_added=int(request.data['quantity'])

        # item_quantity=item_quantity + quantity_added
        # item.save()
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(item=item)

            inventory_data=serializer.data

            response={
                "data":{
                    "user":dict(inventory_data),
                    "status":"success", 
                    "message":"New Store Inventory Added Successfully"
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllStoreInventory(APIView):
    serializer_class=AddNewInventory

    def get(self, request, format=None):
        store_inventory=Inventory.objects.all()
        serializers=AddNewInventory(store_inventory, many=True)
        # print(store_inventory)
        return Response(serializers.data)


class UpdateStoreInventoryView(generics.CreateAPIView):
    serializer_class=UpdateStoreInventory

    def post(self, request, *args, **kwargs):
        item_id=self.kwargs["pk"]
        print(item_id)

        serializer=self.serializer_class(data=request.data)

        item=Inventory.objects.get(id=item_id)
        print(item.quantity)

        item_quantity=item.quantity
        new_added_quantity=request.data["quantity"]
        print(new_added_quantity)

        new_total_quantity = int(item.quantity) + int(new_added_quantity)
        print(new_total_quantity)

        item.quantity=new_total_quantity
        print(item.quantity)
        item.save()

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response = {
                "data":{
                    "status":"Success", 
                    "message":"Inventory data updated successfully"
                }
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SellStoreInventoryView(generics.CreateAPIView):
    serializer_class=SellStoreInventory

    def post(self, request, *args, **kwargs):
        item_id=self.kwargs["pk"]
        print(item_id)

        serializer=self.serializer_class(data=request.data)

        item=Inventory.objects.get(id=item_id)
        print(item.quantity)

        item_quantity=item.quantity
        new_added_quantity=request.data["quantity"]
        print(new_added_quantity)

        new_total_quantity = int(item.quantity) - int(new_added_quantity)
        print(new_total_quantity)

        item.quantity=new_total_quantity
        print(item.quantity)
        item.save()

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response = {
                "data":{
                    "status":"Success", 
                    "message":"Inventory balance has been updated"
                }
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        

