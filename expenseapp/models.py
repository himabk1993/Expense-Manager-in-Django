from django.db import models
from signup.models import UserProfileInfo

class Shop(models.Model):
    shop_name = models.CharField(max_length = 200)

class Category(models.Model):
    category_name = models.CharField(max_length = 100)

class PayMode(models.Model):
    payed_by = models.CharField("cost payed by", max_length = 100)

class Expense(models.Model):
    user = models.ForeignKey(UserProfileInfo, on_delete = models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    payed_by = models.ForeignKey(PayMode, on_delete = models.CASCADE)
    item = models.CharField(max_length = 100)
    quantity = models.DecimalField(max_digits = 10, decimal_places = 3)
    rate = models.DecimalField(max_digits = 20, decimal_places = 5)
    purchase_date = models.DateTimeField("purchased date")
    description = models.CharField("Extra notes on the purchase", default="NILL", max_length = 1000)
    entered_date = models.DateTimeField("data added date")
