from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    shared_with = models.ManyToManyField(User, related_name='shared_budgets', blank=True)

class Income(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
