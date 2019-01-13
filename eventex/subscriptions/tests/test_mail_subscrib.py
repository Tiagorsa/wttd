from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Tiago Sá', cpf='12345678901', email='tiagosa@hotmail.com', phone='91-98424-5276')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subcripton_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subcripton_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subcripton_email_to(self):
        expect = ['contato@eventex.com.br', 'tiagosa@hotmail.com']

        self.assertEqual(expect, self.email.to)


    def test_subscription_body(self):
        contents = ['Tiago Sá','12345678901','tiagosa@hotmail.com', '91-98424-5276']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

