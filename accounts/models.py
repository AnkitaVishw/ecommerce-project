from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    CUSTOMER = "customer"
    SELLER = "seller"

    ROLE_CHOICES = [
        (CUSTOMER, "Customer"),
        (SELLER, "Seller"),
    ]

    phone = models.CharField(max_length=15, blank=True)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=CUSTOMER
    )

    shop_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username