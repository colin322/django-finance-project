from django.contrib.auth.models import User
from django.db import models
from .goal_model import Goal

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
