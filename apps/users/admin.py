from django.contrib import admin

from .models import User


class UserCustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'is_active']
    search_fields = ['username', 'full_name', 'email']


admin.site.register(User, UserCustomAdmin)
