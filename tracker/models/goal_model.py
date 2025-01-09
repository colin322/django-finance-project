from django.contrib.auth.models import User
from django.db import models

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
