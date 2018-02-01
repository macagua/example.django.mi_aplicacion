# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CentroComercial(models.Model):
    name = models.CharField(max_length=200)


class Local(models.Model):
    local = models.ForeignKey(CentroComercial, on_delete=models.CASCADE,
                              related_name='locales_centro_comercial')
    name = models.CharField(max_length=200)


class CategoriaLocal(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE,
                              related_name='categoria_local',
                              blank=True, null=True)
    name = models.CharField(max_length=200)
