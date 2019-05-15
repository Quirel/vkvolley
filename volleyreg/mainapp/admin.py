from django.contrib import admin

from mainapp.models import Player

admin.site.site_header = 'VolleyReg administration'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'registered']
    list_display_links = ['name']
    list_editable = ['date']
    ordering = ('id',)

