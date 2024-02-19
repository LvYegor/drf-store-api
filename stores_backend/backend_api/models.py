from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    established = models.DateField()
    floor_area = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    specs = models.TextField()
    rating = models.PositiveIntegerField()
    supplier_info = models.TextField()
    made_in = models.CharField(max_length=255)
    production_company_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class ProductComment(models.Model):
    author = models.CharField(max_length=255)
    message = models.TextField()
    rating = models.PositiveIntegerField()
    posted = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.author} on {self.product.name}"
