from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from categories.models import Category
from trip.models import Trip

User = get_user_model()


class TestUrls(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create_user(
            username='auth'
        )

        cls.category = Category.objects.create(
            title='test_cat',
            slug='test_cat',
        )
        cls.trip = Trip.objects.create(
            title='Test_trip',
            slug='test-trip',
            date='2010-01-01',
            published=True,
            category_id=1,
            user=TestUrls.user
        )

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_pages(self) -> None:
        pages: tuple = ('add/', 'about/', 'search/', 'terms_of_use/', '')
        client = self.guest_client
        for page in pages:
            response = client.get(page)
            error_name: str = f'Error: not connection with page {page}'
            self.assertEqual(response.status_code, HTTPStatus.OK, error_name)

    def test_correct_static_templates_for_urls(self) -> None:
        templates_url_names: dict = {
            '': 'trip/index.html',
            '/ru/': 'trip/index.html',
            '/en/': 'trip/index.html',
            '/ru/about/': 'trip/about.html',
            '/en/about/': 'trip/about.html',
            '/ru/terms_of_use/': 'trip/terms_of_use.html',
            '/en/terms_of_use/': 'trip/terms_of_use.html',
            ' ': 'trip/404.html'
        }
        client = self.guest_client
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.client.get(address)
                error_name: str = f'Error {address} wait template {template}'
                self.assertTemplateUsed(response, template, error_name)

    def test_urls_guest_client(self):
        pages: tuple = ('',
                        f'/ru/about/',
                        f'/ru/trip/{self.trip.slug}/',
                        f'/en/about/',
                        f'/en/trip/{self.trip.slug}/')
        client = self.guest_client
        for page in pages:
            response = client.get(page)
            error_name = f'Error: not access for page {page}'
            self.assertEqual(response.status_code, HTTPStatus.OK, error_name)

    def test_urls_redirect_guest_client(self):
        url1 = '/ru/users/login/?next=/ru/add/'
        url2 = '/en/users/login/?next=/en/add/'
        url3 = f'/ru/users/login/?next=/ru/edit/{self.trip.slug}/'
        url4 = f'/en/users/login/?next=/en/edit/{self.trip.slug}/'
        url5 = f'/ru/users/login/?next=/ru/delete/{self.trip.slug}/'
        url6 = f'/en/users/login/?next=/en/delete/{self.trip.slug}/'

        pages = {
            '/ru/add/': url1,
            '/en/add/': url2,
            f'/ru/edit/{self.trip.slug}/': url3,
            f'/en/edit/{self.trip.slug}/': url4,
            f'/ru/delete/{self.trip.slug}/': url5,
            f'/en/delete/{self.trip.slug}/': url6,
        }
        client = self.guest_client
        for page, value in pages.items():
            response = client.get(page)
            self.assertRedirects(response, value)

    def test_urls_authorized_client(self):
        pages: tuple = ('/ru/add/',
                        f'/ru/edit/{self.trip.slug}/',
                        f'/ru/delete/{self.trip.slug}/')

        for page in pages:
            response = self.authorized_client.get(page)
            error_name = f'Error: not access for {page}'
            self.assertEqual(response.status_code, HTTPStatus.OK, error_name)

    def test_correct_templates_uses(self):
        templates_url_names: dict = {
            '': 'trip/index.html',
            '/ru/': 'trip/index.html',
            '/en/': 'trip/index.html',
            '/ru/about/': 'trip/about.html',
            '/en/about/': 'trip/about.html',
            '/ru/terms_of_use/': 'trip/terms_of_use.html',
            '/en/terms_of_use/': 'trip/terms_of_use.html',
            ' ': 'trip/404.html',
            '/ru/add/': 'trip/add.html',
            '/en/add/': 'trip/add.html',
        }

        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                error_name = f'Error: {address} for template {template}'
                self.assertTemplateUsed(response, template, error_name)

    def test_correct_delete_and_edit_trip_template_for_owner(self):

        templates_url_names: dict = {
            f'/ru/delete/{self.trip.slug}/': 'trip/delete.html',
            f'/en/delete/{self.trip.slug}/': 'trip/delete.html',
            f'/ru/edit/{self.trip.slug}/': 'trip/add.html',
            f'/en/edit/{self.trip.slug}/': 'trip/add.html',
        }
        for address, value in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                error_name = f'Error: {address} for template {value}'
                self.assertTemplateUsed(response, value, error_name)

    def test_url_search_template(self):
        search = f'aaa'
        templates_url_names: dict = {
            f'/ru/search/?search={search}/': 'trip/index.html',
            f'/en/search/?search={search}/': 'trip/index.html',
        }
        for address, value in templates_url_names.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, value)


