from django.contrib import admin

from .models import Cheese


@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):
    pass

