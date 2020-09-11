"""
Project    : "CCRH"
module     : master/admin
created    : 03/03/2020
Author     : Manish Kumar
"""

from django.contrib import admin
from master.models import (News,
                           Downloads,
                           QuickLink,
                           Media,
                           )
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, IntegerWidget
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin
from import_export.formats import base_formats
from django.forms import forms, ModelForm, Select
from django.contrib import admin
from import_export import resources, fields
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_headline', 'desc')
    search_fields = ('news_headline',)
    
class DownloadsAdmin(admin.ModelAdmin):
    list_display = ('download_headline', 'desc')
    search_fields = ('download_headline',)
    
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ('headline', 'link')
    search_fields = ('headline',)
    
class MediaAdmin(admin.ModelAdmin):
    list_display = ('headline', )
    search_fields = ('headline',)

    
admin.site.register(News, NewsAdmin)
admin.site.register(Downloads, DownloadsAdmin)
admin.site.register(QuickLink, QuickLinkAdmin)
admin.site.register(Media, MediaAdmin)
