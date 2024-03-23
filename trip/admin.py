from django.contrib import admin

from trip.models import Trip


# Register your models here.

class TripAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Trip, TripAdmin)
