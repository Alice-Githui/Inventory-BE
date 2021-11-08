from django.urls import path
from .models import *
from .views import *

urlpatterns=[
    path("add-store-inventory/", AddStoreInventory.as_view(), name="add-store-inventory"),

]