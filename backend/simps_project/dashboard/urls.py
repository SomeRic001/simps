from django.urls import path
from . import views

urlpatterns = [
    # Income URLs
    path('add-income/', views.add_income, name='add_income'),
    path('get-income/', views.get_income, name='get_income'),
    path('update-income/', views.update_income, name='update_income'),
    path('delete-income/', views.delete_income, name='delete_income'),
    
    # Expenses URLs
    path('add-expense/', views.add_expense, name='add_expense'),
    path('get-expenses/', views.get_expenses, name='get_expenses'),
    path('update-expense/', views.update_expense, name='update_expense'),
    path('delete-expense/', views.delete_expense, name='delete_expense'),
    
    # Savings URLs
    path('calculate-savings/', views.calculate_savings, name='calculate_savings'),
    path('get-savings/', views.get_savings, name='get_savings'),
]