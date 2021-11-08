from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username=models.CharField(max_length=255, unique=True)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255, default="")
    

    def __str__(self):
        return self.username

class Inventory(models.Model):
    name=models.CharField(max_length=500)
    quantity=models.IntegerField(default=0)
    buying_price=models.IntegerField()
    selling_price=models.IntegerField()
    description=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

