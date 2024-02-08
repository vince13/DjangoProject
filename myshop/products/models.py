from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="product_pics")
    created_by = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
