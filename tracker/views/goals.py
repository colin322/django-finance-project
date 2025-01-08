from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..forms import GoalForm
from ..models import Goal

@login_required
def goals(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user  
            goal.save()
            return redirect('doelen')  
    else:
        form = GoalForm()

    doelen = Goal.objects.filter(user=request.user)

    return render(request, "goals.html", {"form": form, "doelen": doelen})



@login_required
def delete_goal(request, id):
    goal = get_object_or_404(Goal, id=id, user=request.user)

    goal.delete()

    return redirect('doelen')

@login_required
def mark_as_completed(request, id):
    goal = get_object_or_404(Goal, id=id, user=request.user)

    if request.method == "POST":
        goal.completed = not goal.completed
        goal.save()

    return redirect('doelen') 


