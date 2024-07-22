from django.test import TestCase
from django.db import IntegrityError

from categories.models import Category
from trip.models import Trip


class ModelTripTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            title='Hike',
            slug='hike',
        )
        cls.trip = Trip.objects.create(
            title='Test_trip',
            slug='test-trip',
            date='2010-01-01',
            published=True,
            category_id=1,
        )

        cls.trip_2 = Trip.objects.create(
            title='Test_trip_2',
            slug='test-trip-2',
            date='2010-01-01',
            published=True,
            category_id=1,
        )

    def test_title_verbose(self):
        trip = ModelTripTest.trip
        title = trip._meta.get_field('title').verbose_name
        self.assertEquals(title, 'Title')

    def test_title_var(self):
        trip = ModelTripTest.trip
        var = trip.title
        self.assertEquals(var, 'Test_trip')

    def test_slug_verbose(self):
        trip = ModelTripTest.trip
        slug = trip._meta.get_field('slug').verbose_name
        self.assertEquals(slug, 'Slug')

    def test_slug_var(self):
        trip = ModelTripTest.trip
        var = trip.slug
        self.assertEquals(var, 'test-trip')

    def test_slug_unique(self):
        trip = ModelTripTest.trip
        trip_2 = ModelTripTest.trip_2
        slug = trip.slug
        slug_2 = trip_2.slug
        self.assertNotEqual(slug, slug_2)

    def test_date_verbose(self):
        trip = ModelTripTest.trip
        date = trip._meta.get_field('date').verbose_name
        self.assertEquals(date, 'Date')

    def test_date_var(self):
        trip = ModelTripTest.trip
        date = trip.date
        self.assertEquals(date, '2010-01-01')

    def test_absolute_url(self):
        trip = ModelTripTest.trip
        self.assertEquals(trip.get_absolute_url(), f'/en-us/trip/{self.trip.slug}/')
