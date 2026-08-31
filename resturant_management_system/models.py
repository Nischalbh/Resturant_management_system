from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Table(models.Model):
        number = models.CharField(max_length=200)
        capacity = models.IntegerField()
        is_available = models.BooleanField(default=True)

        def __str__(self):
            return f"Table no. {self.number} - {self.is_available}"


class Order(models.Model):
    Status_Choice = [("p", "pending"), ("ip", "In Progress"), ("C", "Completed")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    Status = models.CharField(max_length=2, choices=Status_Choice, default="p")
    payment_status = models.BooleanField(default=False)
