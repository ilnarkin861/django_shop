from django.contrib import admin
from .models import *

class CenterInfoInline(admin.StackedInline):
    model = CenterInfo


class CityAdmin(admin.ModelAdmin):
    list_per_page = 20
    save_on_top = True
    inlines = [CenterInfoInline]

class CenterInfoAdmin(admin.ModelAdmin):

    list_display = ('get_center_name', 'openning_hours', 'address',)
    list_editable = ('openning_hours', 'address',)
    list_filter = ('city',)
    list_per_page = 20
    save_on_top = True


admin.site.register(City, CityAdmin)
admin.site.register(CenterInfo, CenterInfoAdmin)

