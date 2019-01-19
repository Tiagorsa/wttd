from django.test import TestCase
from eventex.core.models import Speaker
from django.shortcuts import resolve_url as r


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            description='Programadora e almirante',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site'
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_descrition_can_be_blank(self):
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_descrition_can_be_website(self):
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_get_absolute_url(self):
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())
