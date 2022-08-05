from tkinter import SW
from django.db import models
from django.conf import settings
from apps.order.models import Order

class Payment(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True, blank=True, db_column='payment_date')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_type = models.CharField(max_length=100) # TODO: limitar à choices

    class Meta:
        db_table = 'payment'
