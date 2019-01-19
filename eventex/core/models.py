from django.db import models
from django.shortcuts import resolve_url as r



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

    #name = 'Grace Hopper'
    #website = 'http://hbn.link/hopper-site'
    #slug = 'grace-hopper'
    #photo = 'http://hbn.link/hopper-pic'
    #description = 'Programadora e almirante'
    ##description = 'Programadora e almirante<br/>Inventora do compulador, criadora da linguagem de programação Flow-Matic serviu de base para a linguagem COBOL permitindo a popularização das aplicações comerciais.'
