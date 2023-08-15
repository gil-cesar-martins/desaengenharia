from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app import views

urlpatterns = [
    path('painelcontrole/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = 'DESA ENGENHARIA'
admin.AdminSite.site_title = 'DESA ENGENHARIA'
admin.AdminSite.index_title = 'Área Administrativa'