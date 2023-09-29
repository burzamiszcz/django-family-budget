from django.urls import path
from .views import *

urlpatterns = [
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>', BudgetDetailsView.as_view(), name='budget-details'),
]