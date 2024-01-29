from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthday'
    ]
    list_editable = [
        'first_name',
        'last_name',
        'birthday'
    ]
    list_display_links = list_display = [
        'first_name'
    ]

    admin.site.register(Birthday)
