from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..forms import TransactionForm
from ..models import UserInfo, Transaction

@login_required
def transactions(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            user_info = UserInfo.objects.get(user=request.user)
            
            amount = form.cleaned_data['amount'] 
            choice = form.cleaned_data['category'] 
            
            if choice == "expense":
                user_info.saved_money -= amount
            else:
                user_info.saved_money += amount  
            user_info.save()
            
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            
            return redirect('/Transacties')
    else:
        form = TransactionForm()
    
    transactions = Transaction.objects.filter(user=request.user)

    return render(request, "transactions.html", {"form": form, "transactions": transactions})


def remove_transaction(request, transaction_id):
    user_info = UserInfo.objects.get(user=request.user)
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if transaction.category == "income":
        user_info.saved_money -= transaction.amount
    else:
        user_info.saved_money += transaction.amount
    user_info.save()
    transaction.delete()
    return redirect('/Transacties')