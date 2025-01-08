from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile', views.edit_profile, name='edit_profile'),
    path("Gegevens/", views.gegevens, name="gegevens"),
    path('Rapporten/', views.rapports, name='rapporten'),
    path('Transacties/', views.transactions, name='transacties'),
    path('Doelen/', views.goals, name='doelen'),
    path('Transacties/<int:transaction_id>/remove/', views.remove_transaction, name='remove_transaction'),
    path('Doelen/verwijder/<int:id>/', views.delete_goal, name='delete_goal'),
    path('Doelen/compleet/<int:id>/', views.mark_as_completed, name='mark_as_completed'),
]
