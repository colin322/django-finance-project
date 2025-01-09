from django.contrib.auth.models import User
from django.db import models

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[('income', 'Inkomen'), ('expense', 'Uitgave')])
    date = models.DateField()
