from django.db import models
from django.contrib.auth.models import User

class Categoory(models.Model):
    name = models.CharField(max_length=133)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=134, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=75, null=True, blank=True)
    cerated_data = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categoory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
















