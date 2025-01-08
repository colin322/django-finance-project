from django import forms
from django.contrib.auth.models import User
from .models import UserInfo, Goal, Transaction

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

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

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'monthly_budget']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. Vakantie sparen'
            }),
            'target_amount': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 5000 (Doelbedrag)'
            }),
            'monthly_budget': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Bijv. 1000 (Hoeveel je er maandelijks aan wilt uitgeven)'
            }),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input block w-full mt-1 border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'}),
        }
