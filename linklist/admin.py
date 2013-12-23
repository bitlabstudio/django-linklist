"""Admin objects for the ``linklist`` app."""
from django.contrib import admin

from . import models


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'position')
    list_editable = ('position', )


class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.LinkCategory, LinkCategoryAdmin)
