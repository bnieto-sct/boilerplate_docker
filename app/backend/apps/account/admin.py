from django.contrib import admin

from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "username", "testing")
    list_filter = ("testing",)
    search_fields = ("first_name", "last_name", "username")
