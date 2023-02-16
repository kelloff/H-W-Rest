# DRF
from rest_framework.routers import DefaultRouter

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (include, path)

# First party
from main.views import CarViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

router: DefaultRouter = DefaultRouter(
    trailing_slash=False,
)
router.register('', CarViewSet)

urlpatterns += [
    path('api/v1/', include(router.urls))
]