from django.shortcuts import render
# from rest_framework.views import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import serializers,status
from django.core.checks import messages
from .serializers import *
from django.http import Http404

# Create your views here.

class RegisterNewUserView(generics.CreateAPIView):
    serializer_class=RegisterNewUserSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            user_data=serializer.data

            response={
                "data":{
                    "user":dict(user_data),
                    "status":"Success",
                    "message":"New User registered successfully"
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AddStoreInventory(generics.CreateAPIView):
    serializer_class=AddNewInventory

    def post(self, request, *args, **kwargs):

        serializer=self.serializer_class(data=request.data)

        # item=Inventory.objects.get(pk=item_id)
        # item_quantity=item.quantity
        # print(item_quantity)

        # quantity_added=int(request.data['quantity'])

        # item_quantity=item_quantity + quantity_added
        # item.save()
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()

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


class UpdateStoreInventoryView(APIView):
    
    def get_store_item(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None):
        store_item=self.get_store_item(pk)
        serializers=AddNewInventory(store_item)
        return Response(serializers.data)

    def patch(self, request, *args, **kwargs):
        item_id=self.kwargs["pk"]
        print(item_id)

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

        serializers=UpdateStoreInventory(item, request.data, partial=True)
        print(serializers)

        if serializers.is_valid(raise_exception=True):
            serializers.save(quantity = new_total_quantity)

            product_data = serializers.data

            response = {
                "data":{
                    "quantity":dict(product_data),
                    "status":"Success", 
                    "message":"Inventory data updated successfully"
                }
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SellStoreInventoryView(generics.CreateAPIView):
    serializer_class=SellStoreInventory

    def patch(self, request, *args, **kwargs):
        item_id=self.kwargs["pk"]
        print(item_id)

        serializer=self.serializer_class(data=request.data)

        item=Inventory.objects.get(id=item_id)
        print(item.quantity)

        item_quantity=item.quantity
        new_added_quantity=request.data["quantity"]
        print(new_added_quantity)

        if item_quantity == 0:
            return Response("You do not have enough items in stock")
        else:
            new_total_quantity = int(item.quantity) - int(new_added_quantity)
            print(new_total_quantity)

            item.quantity=new_total_quantity
            print(item.quantity)
            item.save()

        if serializer.is_valid(raise_exception=True):
            serializer.save(item_quantity = new_total_quantity)

            response = {
                "data":{
                    "status":"Success", 
                    "message":"Inventory balance has been updated"
                }
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteStoreInventoryView(APIView):
    def get_store_item(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format=None):
        store_item=self.get_store_item(pk)
        serializers=AddNewInventory(store_item)
        return Response(serializers.data)

    #   # put request to update an existing application
    # def put(self, request, pk, format=None):
    #     application=self.get_application(pk=pk)
    #     serializers=ApplicationSerializer(application, request.data)
    #     if serializers.is_valid(raise_exception=True):
    #         serializers.save()
    #         return Response(serializers.data)
    #     else:
    #         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        store_item=self.get_store_item(pk)
        store_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        

