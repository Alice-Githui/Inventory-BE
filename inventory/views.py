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

    def post(self, request, format=None):
        serializer=self.serializer_class(data=request.data)
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

