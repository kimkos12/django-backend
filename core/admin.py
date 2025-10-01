
# Register your models here.

from django.contrib import admin
from .models import Contact, Project

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")
    search_fields = ("name", "email")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "created_at")
    search_fields = ("title",)

