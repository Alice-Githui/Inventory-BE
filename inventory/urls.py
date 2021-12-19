from django.urls import path
from .models import *
from .views import *

urlpatterns=[
    path("register-new-user/", RegisterNewUserView.as_view(), name="register-new-user"),
    path("get-products/", GetAllStoreInventory.as_view(), name="get-all-storeinventory"),
    path("add-product/", AddStoreInventory.as_view(), name="add-store-inventory"),
    path("update-product/<int:pk>/", UpdateStoreInventoryView.as_view(), name="update-store-inventory"),
    path("sell-product/<int:pk>/", SellStoreInventoryView.as_view(), name="sell-store-inventory"),
    path("delete-product/<int:pk>/", DeleteStoreInventoryView.as_view(), name="delete-store-inventory")

]