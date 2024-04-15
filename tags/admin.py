from django.contrib import admin

from tags.models import Tag


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag',)}


admin.site.register(Tag, TagAdmin)
