from django.contrib import admin
from django.urls import path
from django.urls import (
    path, 
    include
)
from main.views import (
    CarView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('cars/' , CarView.as_view())
]
