from django.urls import path

from tags.views import TripTag, ShowAllTags, AddTag

urlpatterns = [
    path('tag/', ShowAllTags.as_view(), name='all_tags'),
    path('tag/add', AddTag.as_view(), name='add_tag'),
    path('tag/<slug:slug>/', TripTag.as_view(), name='tag'),
]

