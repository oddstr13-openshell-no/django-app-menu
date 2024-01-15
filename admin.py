from django.contrib import admin

from menu.models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "visibility", "order")
    list_filter = ["visibility"]
    search_fields = ["title", "url"]

    ordering = ("order",)


admin.site.register(MenuItem, MenuItemAdmin)
