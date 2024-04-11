from django.urls import path

from images.views import ShowGallery

urlpatterns = [
    path('gallery/', ShowGallery.as_view(), name='gallery')
]

