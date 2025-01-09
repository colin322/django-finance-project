from django import forms
from ..models import Goal

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
