from django.urls import path

from trip.views import TripList, ShowTrip, AddTrip, EditTrip

urlpatterns = [
    path('', TripList.as_view(), name='home'),
    path('add/', AddTrip.as_view(), name='add'),
    path('edit/<slug:slug>/', EditTrip.as_view(), name='edit'),
    path('trip/<slug:slug>/', ShowTrip.as_view(), name='trip'),


]

