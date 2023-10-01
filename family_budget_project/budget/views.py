from rest_framework import generics, status, serializers
from .models import Budget, Income, Expense
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import BudgetSerializer, IncomeSerializer, ExpenseSerializer, ShareBudgetSerializer
from rest_framework.pagination import PageNumberPagination
from .pagination import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BudgetFilter

class BudgetListCreateView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BudgetFilter

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
    serializer_class = BudgetSerializer
    
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


class IncomeCreateView(generics.CreateAPIView):
    serializer_class = IncomeSerializer

    def perform_create(self, serializer):
        budget_id = self.kwargs.get('budget_id')
        budget = Budget.objects.get(pk=budget_id, user=self.request.user)
        serializer.save(budget=budget)

class ExpenseCreateView(generics.CreateAPIView):
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        budget_id = self.kwargs.get('budget_id')
        budget = Budget.objects.get(pk=budget_id, user=self.request.user)
        serializer.save(budget=budget)


class ShareBudgetUpdateView(generics.UpdateAPIView):
    serializer_class = ShareBudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def get_object(self):
        budget = super().get_object()
        return budget
    
    def perform_update(self, serializer):
        users_to_share_with = serializer.validated_data.get('shared_with')
        for user in users_to_share_with:
            try:
                user_object = User.objects.get(username=user.username)
                budget = self.get_object()
                budget.shared_with.add(user_object)
            except User.DoesNotExist:
                raise serializers.ValidationError(f"User with username {user.username} does not exist.")

        return Response('Users added to budget successfully', status=status.HTTP_200_OK)
    

class ShareBudgetDeleteView(generics.DestroyAPIView):
    serializer_class = ShareBudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def get_object(self):
        budget = super().get_object()
        return budget
    
    def perform_destroy(self, instance):
        user_to_remove = self.request.data.get('username')
        try:
            user = User.objects.get(username=user_to_remove)
            instance.shared_with.remove(user)
            return Response({'message': f'User {user_to_remove} removed from budget sharing successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")