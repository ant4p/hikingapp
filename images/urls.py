from django.urls import path

from images.views import ShowGallery

app_name = 'image'

urlpatterns = [
    path('gallery/', ShowGallery.as_view(), name='gallery'),
]

