from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Tiago Sá',
            cpf='12345678901',
            email='tiagosa@hotmail.com',
            phone='91-98424-5276'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def teste_str(self):
        self.assertEqual('Tiago Sá', str(self.obj))

    def test_paid_default_to_false(self):
        """must default paid must be false"""
        self.assertEqual(False, self.obj.paid)