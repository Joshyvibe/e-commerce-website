from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('online_site.urls')),
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name='online_site/robots.txt', content_type='text/plain')),
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

