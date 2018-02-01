# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CentroComercial(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Centro Comercial"
        verbose_name_plural = "Centro Comerciales"

    def __unicode__(self):
        return "%s" % (self.name)

    def __str__(self):
        return self.name


class CategoriaLocal(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categoria de Local"
        verbose_name_plural = "Categorias de Locales"

    def __unicode__(self):
        return "%s" % (self.name)

    def __str__(self):
        return self.name


class Local(models.Model):
    centro_comercial = models.ForeignKey(CentroComercial, on_delete=models.CASCADE,
                              related_name='locales_centro_comercial',
                              verbose_name='Centro comercial')
    categoria_local = models.ManyToManyField(CategoriaLocal,
                              related_name='categoria_local',
                              verbose_name='Categorias del Local')
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.centro_comercial)

    def __str__(self):
        return self.name
