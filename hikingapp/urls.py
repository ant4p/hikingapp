"""
URL configuration for hikingapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

from hikingapp import settings
from trip.views import handler_403, handler_404, handler_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trip.urls')),
    path('category/', include('categories.urls', namespace='cat')),
    path('image/', include('images.urls', namespace='image')),
    path('tag/', include('tags.urls', namespace='tag')),
    path('users/', include('users.urls', namespace='users')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('social/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler_404
handler403 = handler_403
handler500 = handler_500
