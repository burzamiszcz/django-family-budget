from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Budget  # Zaimportuj odpowiedni model
from django.contrib.auth.models import User

class BudgetUpdateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.budget = Budget.objects.create(user=self.user, title='Test Budget')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')
        self.shared_users = [User.objects.create(username='user1'), User.objects.create(username='user2')]

    def test_perform_update(self):
        shared_users_ids = [user.id for user in self.shared_users]
        data = {
            "shared_with": shared_users_ids
            }
        url = reverse('share-budget-update', kwargs={'pk': self.budget.pk})
        response = self.client.put(url, data = data, format = 'json')
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_perform_update(self):
        shared_users_ids = [user.id for user in self.shared_users]
        data = {
            "shared_with": shared_users_ids
        }
        url = reverse('share-budget-update', kwargs={'pk': self.budget.pk + 1})
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, 404)