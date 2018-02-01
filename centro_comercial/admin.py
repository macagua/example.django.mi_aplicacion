# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from centro_comercial.models import CentroComercial, Local, CategoriaLocal


class CentroComercialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_per_page = 10


class LocalAdmin(admin.ModelAdmin):
    list_display = ['id', 'centro_comercial', 'categoria_local', 'name']
    list_display_links = ('centro_comercial', 'categoria_local', 'name')
    search_fields = ['name']
    list_filter = ('centro_comercial', 'name')
    list_per_page = 10


class CategoriaLocalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('name')
    search_fields = ['name']
    list_filter = ('name')
    list_per_page = 10

admin.site.register(CentroComercial)
admin.site.register(Local)
admin.site.register(CategoriaLocal)
