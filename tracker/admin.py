from django.contrib import admin
from .models import UserInfo, Transaction, Goal, SavingsAccountData

admin.site.register(UserInfo)
admin.site.register(Transaction)
admin.site.register(Goal)
admin.site.register(SavingsAccountData)