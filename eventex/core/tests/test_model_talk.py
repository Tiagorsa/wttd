from django.test import TestCase
from eventex.core.models import Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra',
            #start='10:00',
            #description='Descrição da palestra.'
        )

    def test_Create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        self.talk.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_dreciption_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def speakers_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_blanks(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))
