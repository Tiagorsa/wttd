from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(name='Tiago Sá',
                    cpf='12345678901',
                    email='tiagosa@hotmail.com',
                    phone='91-98424-5276')

        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)


    def test_html(self):
        contexts = (self.obj.name,
                    self.obj.cpf,
                    self.obj.email,
                    self.obj.phone)

        with self.subTest():
            for context in contexts:
                self.assertContains(self.resp, context)


class subscritionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)