from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    monthly_income_netto = models.IntegerField(default=0)
    saved_money = models.IntegerField(default=0)
    groceries = models.IntegerField(default=0)
    rent = models.IntegerField(default=0)
    entertainment = models.IntegerField(default=0)
    others = models.IntegerField(default=0)

    @property
    def monthly_expenses(self):
        base_expenses = self.groceries + self.rent + self.entertainment + self.others
        goal_budgets = Goal.objects.filter(user=self.user).values_list('monthly_budget', flat=True)
        total_goal_budget = sum(goal_budgets)
        return base_expenses + total_goal_budget

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[('income', 'Inkomen'), ('expense', 'Uitgave')])
    date = models.DateField()

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class SavingsAccountData(models.Model):
    def get_default_months():
        return {month: 0 for month in [
            'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
            'september', 'october', 'november', 'december']}
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField(default=datetime.now().year)
    months = models.JSONField(default=get_default_months)
