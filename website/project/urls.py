from django.conf.urls import patterns, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
                       (r'^', include('website.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^ckeditor/', include('ckeditor.urls')),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
