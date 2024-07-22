from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from http import HTTPStatus

from django.urls import reverse

from categories.models import Category
from trip.forms import AddTripForm
from trip.models import Trip
from users.forms import RegisterUserForm

User = get_user_model()


class TestForms(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            title='test_cat',
            slug='test_cat',
        )
        cls.empty_form = AddTripForm(data={})
        cls.user = User.objects.create(
            username='auth'
        )
        cls.data = AddTripForm(data={
            'title': 'Test_trip_1',
            'slug': 'test-trip-1',
            'title_photo': None,
            'date': '2010-01-01',
            'content': 'aaa',
            'published': True,
            'category': TestForms.category,
            'image': None,
            'tag': None,
        })

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_AddTripForm_valid_data(self):
        form = TestForms.data
        self.assertTrue(form.is_valid())

    def test_AddTripForm_is_empty(self):
        form = TestForms.empty_form
        self.assertFalse(form.is_valid())

    def test_obligatory_fields(self):
        form = TestForms.empty_form
        self.assertEquals(len(form.errors), 3)

    # def test_create_trip(self):
    #     trip_count = Trip.objects.count()
    #     form_data = TestForms.data
    #     form_data.slug = 'test-trip-1'
    #     print(form_data)
    #
    #     response = self.authorized_client.post(f'trip/{self.data.slug}/',
    #                                            data=form_data,
    #                                            follow=True)
    #     error_name1 = 'Data is different!'
    #     self.assertTrue(response.status_code, HTTPStatus.OK)