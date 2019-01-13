from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTeste(TestCase):
    def setUP(self):
        self.form = SubscriptionForm()

def test_form_has_fiels(self):
    """ form must have 4 fields """
    expected = ['name', 'cpf', 'email', 'phone']
    self.assertSequenceEqual(expected, list(self.form.fields))
