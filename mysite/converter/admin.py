from django.contrib import admin

from .models import *


class ConverterRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_at', 'image')
    list_display_links = ('id', 'username', 'image')


# class FileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'original_size', 'converted_size')


admin.site.register(ConvertRequest, ConverterRequestAdmin)
admin.site.register(File)
