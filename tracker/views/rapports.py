from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import UserInfo, SavingsAccountData
from tracker.utils import update_savings_balance


@login_required
def rapports(request):
    update_savings_balance()
    user_info, created = UserInfo.objects.get_or_create(user=request.user)
    
    categories = {
        'Boodschappen': user_info.groceries,
        'Huur': user_info.rent,
        'Entertainment': user_info.entertainment,
        'Overige': user_info.others,
    }

    savings_data = SavingsAccountData.objects.filter(user=request.user).order_by('-year')
    yearly_savings = [
        {
            'year': data.year,
            'savings_per_month': [data.months.get(month, 0) for month in [
                'january', 'february', 'march', 'april', 'may', 'june', 
                'july', 'august', 'september', 'october', 'november', 'december'
            ]]
        }
        for data in savings_data
    ]

    return render(request, 'rapports.html', {
        'user_info': user_info,
        'yearly_savings': yearly_savings,
        'categories': categories,
    })
