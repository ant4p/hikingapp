from django.urls import path

from images.views import AddImages

urlpatterns = [
    path('image/', AddImages.as_view(), name='image')
]

