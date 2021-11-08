from django.urls import path
from .models import *
from .views import *

urlpatterns=[
    path("get-all-store_inventory/", GetAllStoreInventory.as_view(), name="get-all-storeinventory"),
    path("add-store-inventory/", AddStoreInventory.as_view(), name="add-store-inventory"),

]