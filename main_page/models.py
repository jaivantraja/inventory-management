import random
import string
from django.db import models
from django.utils import timezone
# Create your models here.
class Purchase(models.Model):
    gst_number = models.CharField(max_length=15)
    product_name = models.CharField(max_length=25)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    bill_number = models.CharField(max_length=15,primary_key=True)
    date = models.DateTimeField(default=timezone.now)

    def save(self,*args,**kwargs):
        if not self.bill_number:
            self.bill_number=self.unique_bill_number()
        super().save(*args,**kwargs)
    def unique_bill_number(self):
        while True:
            bill_number = self.generate_bill_number()
            if not Purchase.objects.filter(bill_number=bill_number).exists():
                return bill_number
    def generate_bill_number(self):
        return ''.join(random.choices(string.ascii_uppercase+string.digits,k=10))

    def __str__(self):
        return f"GST Number:{self.gst_number}  Bill Number:{self.bill_number}  Product Name:{self.product_name}  Quantity:{self.quantity}  Cost:{self.cost}  Total Cost:{self.total_cost}  Date:{self.date}"

class Sales(models.Model):
    gst_number = models.CharField(max_length=15)
    product_name = models.CharField(max_length=25)
    quantity = models.IntegerField()
    bill_number = models.CharField(max_length=15, primary_key=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    sender_gst=models.CharField(max_length=15,default="None")

    def save(self,*args,**kwargs):
        if not self.bill_number:
            self.bill_number=self.unique_bill_number()
        super().save(*args,**kwargs)
    def unique_bill_number(self):
        while True:
            bill_number=self.generate_bill_number()
            if not Purchase.objects.filter(bill_number=bill_number).exists():
                return bill_number
    def generate_bill_number(self):
        return ''.join(random.choices(string.ascii_uppercase+string.digits,k=10))

    def __str__(self):
        return f"GST Number:{self.gst_number}, Sender GST Number:{self.sender_gst}Bill Number:{self.bill_number},Product Name:{self.product_name},Quantity:{self.quantity},Cost:{self.cost},Total Cost:{self.total_cost},Date:{self.date}"

class Inventory(models.Model):
    gst_number = models.CharField(max_length=15)
    product_name = models.CharField(max_length=25)
    quantity = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f"GST Number:{self.gst_number},Product Name:{self.product_name},Quantity:{self.quantity},Cost:{self.total_cost}"
