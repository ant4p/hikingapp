from django.urls import path

from categories.views import TripCategory, ShowAllCategories

app_name = 'cat'

urlpatterns = [

    path('<slug:slug>/', TripCategory.as_view(), name='categories'),
    path('', ShowAllCategories.as_view(), name='all_categories'),

]

