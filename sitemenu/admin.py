from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class MenuItemsAdmin(DraggableMPTTAdmin, SummernoteModelAdmin):
    fieldsets = (
        (None, {'fields':('title', 'url', 'parent', 'menu', 'description', 'page_template_name', 'is_index_page', 'is_show', 'is_catalogue_link', 'is_delivery_link',)}),
        (u'Мета-теги', {'fields':('meta_title','meta_description', 'meta_keywords')}),
    )
    summernote_fields = ('description',)


admin.site.register(Menu)
admin.site.register(MenuItems, MenuItemsAdmin)


