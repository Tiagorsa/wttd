from django.db import models
from django.shortcuts import resolve_url as r

from eventex.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome',  max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()
    
    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'


#class Talk(models.Model):
#class Activity(models.Model):
class Talk(models.Model):
    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', null=True, blank=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManager()
    
    class Meta:
        #abstract = True
        ordering = ['start']
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'
    
    def __str__(self):
        return self.title 

    #name = 'Grace Hopper'
    #website = 'http://hbn.link/hopper-site'
    #slug = 'grace-hopper'
    #photo = 'http://hbn.link/hopper-pic'
    #description = 'Programadora e almirante'
    ##description = 'Programadora e almirante<br/>Inventora do compulador, criadora da linguagem de programação Flow-Matic serviu de base para a linguagem COBOL permitindo a popularização das aplicações comerciais.'


#class Talk(Activity):
#    pass


class Course(Talk):
    slots = models.IntegerField()
    objects = PeriodManager()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

