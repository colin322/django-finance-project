from django.utils.timezone import now
from .models import SavingsAccountData, UserInfo

def update_savings_balance():
    current_date = now()
    current_month = current_date.strftime('%B').lower()
    current_year = current_date.year

    for user_info in UserInfo.objects.all():
        savings_data, created = SavingsAccountData.objects.get_or_create(
            user=user_info.user, year=current_year
        )

        savings_data.months[current_month] = user_info.saved_money
        savings_data.save()
