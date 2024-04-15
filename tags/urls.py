from django.urls import path

from tags.views import TripTag, ShowAllTags

urlpatterns = [

    path('tag/<slug:slug>/', TripTag.as_view(), name='tag'),
    path('tag/', ShowAllTags.as_view(), name='all_tags'),

]

