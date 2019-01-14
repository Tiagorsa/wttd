import uuid as uuid
from django.db import models


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-amil')
    phone = models.CharField('Telefone', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name_plural='inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name

