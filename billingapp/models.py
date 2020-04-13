from django.db import models


class User(models.Model):
    address_label = models.CharField(max_length=100, unique=True)
    user_address = models.CharField(max_length=32)

    def __str__(self):
        return self.address_label


class Product(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    amount = models.FloatField(blank=False)

    def __str__(self):
        return self.title


class Invoice(models.Model):
    user = models.ManyToManyField(User, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    payment_status = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100)
    tax_amount = models.FloatField(blank=False)
    payment_address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.payment_address)
