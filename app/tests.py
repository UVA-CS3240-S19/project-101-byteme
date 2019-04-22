from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
from django.test.client import RequestFactory
from app.views import create_profile
from app.models import Profile, ProfileModel
import sys
from django.http import HttpResponsePermanentRedirect
from django.utils.encoding import force_text
from django.test.utils import override_settings
from django.conf import settings
# Create your tests here.

#c = Client()
#c.login(username="test", password = "password")
admin = User.objects.create_superuser('myuser', 'ab1cde@virginia.edu', 'password')


class ProfileTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_entries_access(self):
        response = self.client.post(('/profile'), {'name': "Test", 'year': "2020", "major": "CS", "bio": "Test data",
                                                   'skills': "Test data", 'courses': "Test data", 'organizations': "Test data", 'interests': "Test data"})
        self.assertEqual(response.status_code, 301)


class ProfileComponentsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.save()
        #Profile.objects.create(user_id = "ab1cde", name = "Test")

    def test_empty_form(self):
        form = ProfileModel()
        self.assertFalse(form.is_valid())

    def test_only_name_component(self):
        form = ProfileModel({
            'name': "Test",
        })
        self.assertFalse(form.is_valid())

    def test_only_year_component(self):
        form = ProfileModel({
            'year': "2020",
        })
        self.assertFalse(form.is_valid())

    def test_only_major_component(self):
        form = ProfileModel({
            'major': "CS",
        })
        self.assertFalse(form.is_valid())

    def test_all_three_components(self):
        form = ProfileModel({
            'name': "Test",
            'year': "2020",
            'major': "CS",
        })
        self.assertTrue(form.is_valid())

    def test_all_components(self):
        form = ProfileModel({
            'name': "Test",
            'year': "2020",
            'major': "CS",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data",
        })
        self.assertTrue(form.is_valid())


class SignUpTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='ab1cde@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('12345')
        self.user.email = 'ab1cde@virginia.edu'
        self.user.save()

    def test_first_time_login(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 301)

    def test_existing_signin(self):
        login = self.client.login(username='ab1cde@virginia.edu', password='12345')
        # print(self.user.id)
        # self.user.id = 10
        response = self.client.post(('/profile/'), {
            'name': "Test",
            'year': "2020",
            'major': "CS",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data"})
        # print(response)
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/app/published_profile/' + str(self.user.id))
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/profile/')
        self.assertRedirects(response, '/app/published_profile/' + str(self.user.id))


class UpdateProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
                username='ab1cde@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('12345')
        self.user.email = 'ab1cde@virginia.edu'
        self.user.save()
        # set up initial user profile
        login = self.client.login(username='ab1cde@virginia.edu', password='12345')
        response = self.client.post(('/profile/'), {
            'name': "Test",
            'year': "2020",
            'major': "CS",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data"})
        self.assertEqual(response.status_code, 302)

    def test_update_nothing(self):
        response = self.client.post(('/update_profile'))
        self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
        self.assertEqual(response.status_code, 301)

    def test_update_name(self):
        response = self.client.post(('/update_profile'), {'name': "Tester"})
        self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
        self.assertEqual(response.status_code, 301)

    def test_update_year(self):
        response = self.client.post(('/update_profile'), {'year': "2021"})
        self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
        self.assertEqual(response.status_code, 301)

    def test_update_major(self):
        response = self.client.post(('/update_profile'), {'major': "Biology"})
        self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
        self.assertEqual(response.status_code, 301)


    def test_update_all_three(self):
        response = self.client.post(('/update_profile'), {'name':"Test2", 'year': "2019", 'major': "Drama"})
        self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
        self.assertEqual(response.status_code, 301)


class SearchTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
                username='ab1cde@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('12345')
        self.user.email = 'ab1cde@virginia.edu'
        self.user.save()
        # set up initial user profile
        login = self.client.login(username='ab1cde@virginia.edu', password='12345')
        response = self.client.post(('/profile/'), {
            'name': "Test",
            'year': "2020",
            'major': "CS",
            'bio': "Test data",
            'skills': "Java, Python",
            'courses': "CS2150, CS3240",
            'organizations': "UVA",
            'interests': "Test data"})
        self.assertEqual(response.status_code, 302)
        self.client.logout()

    def test_search_username(self):
        self.client = Client()
        self.user = User.objects.create(
            username='xy2zab@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('67899')
        self.user.email = 'xy2zab@virginia.edu'
        self.user.save()
        login = self.client.login(username='xy2zab@virginia.edu', password='67899')
        self.client.post(('/profile/'), {
            'name': "Test2",
            'year': "2020",
            'major': "Bio",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data"})
        response = self.client.post(('/search/'), {
            'search_field': "Test"
        })
        self.assertContains(response, "Test")
        self.assertContains(response, "CS")
        # response = self.client.post(('/search/'), {'Test'})
        # print(response)

    def test_search_course(self):
        self.client = Client()
        self.user = User.objects.create(
            username='xy2zab@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('67899')
        self.user.email = 'xy2zab@virginia.edu'
        self.user.save()
        login = self.client.login(username='xy2zab@virginia.edu', password='67899')
        self.client.post(('/profile/'), {
            'name': "Test2",
            'year': "2020",
            'major': "Bio",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data"})
        response = self.client.post(('/search/'), {
            'search_field': "CS2150"
        })
        self.assertContains(response, "Test")
        self.assertContains(response, "CS")

    def test_search_skill(self):
        self.client = Client()
        self.user = User.objects.create(
            username='xy2zab@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('67899')
        self.user.email = 'xy2zab@virginia.edu'
        self.user.save()
        login = self.client.login(username='xy2zab@virginia.edu', password='67899')
        self.client.post(('/profile/'), {
            'name': "Test2",
            'year': "2020",
            'major': "Bio",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data"})
        response = self.client.post(('/search/'), {
            'search_field': "Java"
        })
        self.assertContains(response, "Test")
        self.assertContains(response, "CS")

    def test_search_empty(self):
        self.client = Client()
        self.user = User.objects.create(
            username='xy2zab@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('67899')
        self.user.email = 'xy2zab@virginia.edu'
        self.user.save()
        login = self.client.login(username='xy2zab@virginia.edu', password='67899')
        self.client.post(('/profile/'), {
            'name': "Test2",
            'year': "2020",
            'major': "Bio",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data"})
        response = self.client.post(('/search/'), {'search_field':""})
        for profile in Profile.objects.all():
            self.assertContains(response, profile.name)
        
    def test_search_noresults(self):
        self.client = Client()
        self.user = User.objects.create(
            username='xy2zab@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('67899')
        self.user.email = 'xy2zab@virginia.edu'
        self.user.save()
        login = self.client.login(username='xy2zab@virginia.edu', password='67899')
        self.client.post(('/profile/'), {
            'name': "Test2",
            'year': "2020",
            'major': "Bio",
            'bio': "Test data",
            'skills': "Test data",
            'courses': "Test data",
            'organizations': "Test data",
            'interests': "Test data"})
        response = self.client.post(('/search/'), {'search_field':"notpresent"})
        self.assertContains(response, "There are no search results.")


class ErrorPageTest(TestCase):
    @override_settings(DEBUG=False)
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
                username='ab1cde@virginia.edu', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('12345')
        self.user.email = 'ab1cde@virginia.edu'
        self.user.save()
        # set up initial user profile
        login = self.client.login(username='ab1cde@virginia.edu', password='12345')
        response = self.client.post(('/profile/'), {
            'name': "Test",
            'year': "2020",
            'major': "CS",
            'bio': "Test data",
            'skills': "Java, Python",
            'courses': "CS2150, CS3240",
            'organizations': "UVA",
            'interests': "Test data"})
        self.assertEqual(response.status_code, 302)
        # self.client.logout()

    # def test_invalid_profile_pk(self):
    #     response = self.client.post(('app/published_profile/200'))
    #     print(response)
    #     # self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
    #     self.assertEqual(response.status_code, 301)
    #
    # def test_invalid_update_profile_pk(self):
    #     response = self.client.post(('app/update_profile/200'))
    #     # self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
    #     self.assertEqual(response.status_code, 301)
    #
    # def test_invalid_app_url(self):
    #     response = self.client.post(('/beans'))
    #     # self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
    #     self.assertEqual(response.status_code, 301)

#c.logout()
User.objects.filter(username=admin.username).delete()