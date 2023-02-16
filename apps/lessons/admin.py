from django.contrib import admin

from typing import Optional

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from .models import Comics


class ComicsAdmin(admin.ModelAdmin):
    """ComicsAdmin."""

    model = Comics
    list_display = [
        'title',
        'price'
    ]
    readonly_fields = (

    )

    def get_readonly_fields(
            self, 
            request: WSGIRequest, 
            obj: Optional[Comics]
        ) -> tuple:
        if not obj:
            return self.readonly_fields
        
        return self.readonly_fields + (
            'price',
        )
    
admin.site.register(Comics, ComicsAdmin)