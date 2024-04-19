from django.urls import path

from tags.views import TripTag, ShowAllTags, AddTag

app_name = 'tag'

urlpatterns = [
    path('', ShowAllTags.as_view(), name='all_tags'),
    path('add/', AddTag.as_view(), name='add_tag'),
    path('<slug:slug>/', TripTag.as_view(), name='tag'),
]

