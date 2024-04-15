from django.urls import path

from categories.views import TripCategory, ShowAllCategories

urlpatterns = [

    path('category/<slug:slug>/', TripCategory.as_view(), name='categories'),
    path('category/', ShowAllCategories.as_view(), name='all_categories'),

]

