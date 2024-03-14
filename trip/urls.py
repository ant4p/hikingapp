from django.urls import path

from trip.views import TripList, ShowTrip

urlpatterns = [
    path('', TripList.as_view(), name='home'),
    path('trip/<slug:trip_slug>/', ShowTrip.as_view(), name='trip'),

]
