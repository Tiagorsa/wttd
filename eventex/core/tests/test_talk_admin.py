from django.contrib import admin
from django.test import TestCase
from eventex.core.admin import TalkModelAdmin, Talk


class TalkModelAdminTest(TestCase):
    def setUp(self):
        Talk.objects.create(
            title='Título da Palestra',
            # start='10:00',
            # description='Descrição da palestra.'
        )
        self.model_admin = TalkModelAdmin(Talk, admin.site)

    def test_TalkAdminModel_Instance(self):
        self.assertIsInstance(self.model_admin, admin.ModelAdmin)

    def test_TalkAdminModel_QuerySet_Instance(self):
        from django.db.models import QuerySet
        self.assertIsInstance(self.model_admin.get_queryset(self), QuerySet)

    def test_TalkAdminModel_QuerySet_Count(self):
        self.assertEqual(self.model_admin.get_queryset(self).count(), 1)
