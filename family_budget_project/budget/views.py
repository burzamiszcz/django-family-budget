from rest_framework import generics, status
from .models import Category, Budget, Income, Expense
from rest_framework.response import Response
from .serializers import CategorySerializer, BudgetSerializer, IncomeSerializer, ExpenseSerializer, BudgetDetailsSerializer


class BudgetListCreateView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BudgetDetailsView(generics.RetrieveAPIView):
    serializer_class = BudgetDetailsSerializer

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def get_object(self):
        budget = super().get_object()
        incomes = Income.objects.filter(budget=budget)
        expenses = Expense.objects.filter(budget=budget)
        return budget, incomes, expenses

    def retrieve(self, request, *args, **kwargs):
        budget, incomes, expenses = self.get_object()
        serializer = self.get_serializer(budget)
        data = serializer.data
        data['incomes'] = IncomeSerializer(incomes, many=True).data
        data['expenses'] = ExpenseSerializer(expenses, many=True).data
        return Response(data)

