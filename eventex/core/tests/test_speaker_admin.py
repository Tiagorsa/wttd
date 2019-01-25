from django.contrib import admin
from django.test import TestCase
from eventex.core.admin import SpeakerModelAdmin, Speaker
from eventex.core.models import Contact


class SpeakerModelAdminTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            description='Programadora e almirante',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site'
        )
        self.speaker.contact_set.create(kind=Contact.EMAIL, value='tiagosa@hotmail.com')
        self.speaker.contact_set.create(kind=Contact.PHONE, value='91-98424-5276')
        self.speakermodel = SpeakerModelAdmin(self.speaker, admin.site)

    def test_SpeakerAdminModel_Instance(self):
        self.assertIsInstance(self.speakermodel, admin.ModelAdmin)

    def test_SpeakerAdminModel_email(self):
        self.assertEqual(str(self.speakermodel.email(self.speaker)), 'tiagosa@hotmail.com')

    def test_SpeakerAdminModel_phone(self):
        self.assertEqual(str(self.speakermodel.phone(self.speaker)), '91-98424-5276')
