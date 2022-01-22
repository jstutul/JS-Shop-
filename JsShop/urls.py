from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_title = 'JS Shop Admin Panel'
admin.site.site_header = 'JS Shop Admin Login'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Shop.urls')),
    path('users/',include('App_Account.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
