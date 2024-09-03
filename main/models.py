from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    status = models.IntegerField(
        choices=(
            (1,'Created'),
            (2,'Paid'),
            (3,'Cancelled'),
        ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment for {self.product} by {self.user}. Status: {self.status}'
    

    def save(self, *args, **kwargs):
        payment = Payment.objects.filter(user=self.user).last()
        print(payment)
        if self.id:
            super().save(*args, **kwargs)
        
        if self.user == payment.user:
            if payment.status < 2 :
                return 0
        super().save(*args, **kwargs)

