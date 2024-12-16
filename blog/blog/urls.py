from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import homepage, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('contact/', contact, name='contact'),
]

# Додаємо обробку медіафайлів під час розробки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
