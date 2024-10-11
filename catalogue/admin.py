from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment
from .models import *


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductCategoryAdmin(SummernoteModelAdmin, DraggableMPTTAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'url', 'parent', 'short_description', 'description', 'image',)}),
        (u'Мета-теги', {'fields': ('meta_title', 'meta_description', 'meta_keywords')}),
    )
    summernote_fields = ('description',)
    save_on_top = True


class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'url', 'vendor_code', 'short_description', 'description', 'price', 'thumbnail', 'category', 'in_stock', 'is_popular',)}),
        (u'Мета-теги', {'fields': ('meta_title', 'meta_description', 'meta_keywords')}),
    )
    search_fields = ('title',)
    list_display = ('title', 'vendor_code', 'price', 'in_stock',)
    list_editable = ('in_stock',)
    list_filter = ('category', 'is_popular', 'in_stock')
    save_on_top = True
    inlines = [ProductImageInline]


admin.site.unregister(Attachment)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)