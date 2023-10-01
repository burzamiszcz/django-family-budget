
from rest_framework import serializers
from .models import Budget, Income, Expense
from django.contrib.auth.models import User

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class ShareBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['shared_with']