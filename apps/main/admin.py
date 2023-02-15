# Python
from typing import (
    Optional,
    Any
)

# Django
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

# Local
from .models import Car
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    """Car admin."""

    models = Car
    list_display = [
        'model',
        'price',
        'owner',
        'brand'
    ]
    readonly_fields = (

    )


    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Car]) -> tuple:
        if not obj:
            return self.readonly_fields
        return self.readonly_fields + (
            'price',
        )


admin.site.register(Car,CarAdmin)