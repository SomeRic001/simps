from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard_home, name='dashboard_home'), 
    path('add-income-page/', views.add_income_page, name='add_income_page'),
    path('add-expense-page/', views.add_expense_page, name='add_expense_page'),
    path('view-income/', views.view_income_page, name='view_income_page'),
    path('view-expenses/', views.view_expenses_page, name='view_expenses_page'),
    path('view-savings/', views.view_savings_page, name='view_savings_page'),
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
