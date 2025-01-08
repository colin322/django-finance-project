from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import UserInfoForm
from ..models import UserInfo

@login_required
def gegevens(request):
    user_info, created = UserInfo.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('/Gegevens')
    else:
        form = UserInfoForm(instance=user_info)

    return render(request, "gegevens.html", {"form": form})
