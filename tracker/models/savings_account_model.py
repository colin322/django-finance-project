from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class SavingsAccountData(models.Model):
    def get_default_months():
        return {month: 0 for month in [
            'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
            'september', 'october', 'november', 'december']}
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField(default=datetime.now().year)
    months = models.JSONField(default=get_default_months)
