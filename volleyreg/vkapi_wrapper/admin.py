from django.contrib import admin

from vkapi_wrapper.models import Keys


@admin.register(Keys)
class KeysAdmin(admin.ModelAdmin):
    list_display = ['id', 'app_id', 'group_id']
    list_display_links = ['id', 'app_id', 'group_id']
    ordering = ('id',)
