from django.contrib import admin
from django.urls import (
    path,
    include
)
from django.conf import settings
from django.conf.urls.static import static
from lessons.views import ComicsView, CustomUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ComicsView.as_view()),
    path('users/', CustomUserView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

#MEDIA + STATIC

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# DEBUG TOOLBAR

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]