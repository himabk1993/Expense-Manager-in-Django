from django.urls import path
from . import views

app_name = 'expenseapp'

urlpatterns = [
    path('expense/', views.add_expense, name = 'add_expense'),
    path('expensereport/', views.view_expense, name = 'view_expense'),
]
