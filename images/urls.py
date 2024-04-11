from django.urls import path

from images.views import ShowGallery, ShowEmptyGallery

urlpatterns = [
    path('gallery/', ShowGallery.as_view(), name='gallery'),
    path('empty_gallery/', ShowEmptyGallery.as_view(), name='empty_gallery'),
]

