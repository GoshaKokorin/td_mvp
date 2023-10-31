from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-docs/', include('td_mvp.apps.api.docs.urls')),

    path('api/', include('td_mvp.apps.api.urls')),
]


admin.site.site_title = ' '
admin.site.site_header = 'TD MVP'
admin.site.index_title = 'Панель управления'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
