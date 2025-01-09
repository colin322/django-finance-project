from django import forms
from ..models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            'monthly_income_netto',
            'saved_money',
            'groceries',
            'rent',
            'entertainment',
            'others'
        ]
        widgets = {
            'monthly_income_netto': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 2500'
            }),
            'saved_money': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 500'
            }),
            'groceries': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 300 (Boodschappen)'
            }),
            'rent': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 700 (Huur)'
            }),
            'entertainment': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 200 (Entertainment)'
            }),
            'others': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 100 (Overige)'
            }),
        }
