from django.contrib import admin

from mainapp.models import Player

admin.site.site_header = 'VolleyReg administration'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'registered']
    list_display_links = ['name']
    ordering = ('id',)
