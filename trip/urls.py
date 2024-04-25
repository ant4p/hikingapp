from django.urls import path

from trip.views import TripList, ShowTrip, AddTrip, DeleteTrip, EditTrip, AboutHikingapp, SearchTrip

urlpatterns = [
    path('', TripList.as_view(), name='home'),
    path('add/', AddTrip.as_view(), name='add'),
    path('edit/<slug:slug>/', EditTrip.as_view(), name='edit'),
    path('delete/<slug:slug>/', DeleteTrip.as_view(), name='delete'),
    path('trip/<slug:slug>/', ShowTrip.as_view(), name='trip'),
    path('about/', AboutHikingapp.as_view(), name='about'),
    path('search/', SearchTrip.as_view(), name='search'),

]

