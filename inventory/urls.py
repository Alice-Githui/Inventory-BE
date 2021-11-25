from django.urls import path
from .models import *
from .views import *

urlpatterns=[
    path("register-new-user/", RegisterNewUserView.as_view(), name="register-new-user"),
    path("get-all-store_inventory/", GetAllStoreInventory.as_view(), name="get-all-storeinventory"),
    path("add-store-inventory/<int:pk>/", AddStoreInventory.as_view(), name="add-store-inventory"),
    path("update-store-inventory/<int:pk>/", UpdateStoreInventoryView.as_view(), name="update-store-inventory"),
    path("sell-store-inventory/<int:pk>/", SellStoreInventoryView.as_view(), name="sell-store-inventory"),
    path("delete-inventory/<int:pk>/", DeleteStoreInventoryView.as_view(), name="delete-store-inventory")

]