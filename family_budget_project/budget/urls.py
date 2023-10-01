from django.urls import path
from .views import *

urlpatterns = [
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>', BudgetDetailsView.as_view(), name='budget-details'),
    path('budgets/<int:pk>/incomes/create/', IncomeCreateView.as_view(), name='income-create'),
    path('budgets/<int:pk>/expenses/create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('budgets/<int:pk>/share/update', ShareBudgetUpdateView.as_view(), name='share-budget-update'),
    path('budgets/<int:pk>/share/delete', ShareBudgetDeleteView.as_view(), name='share-budget-delete'),

]