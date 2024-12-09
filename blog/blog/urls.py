from django.contrib import admin
from django.urls import path, include
from blog.views import homepage
from blog.views import contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('contact/', contact, name='contact'),
]

