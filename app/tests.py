from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
from django.test.client import RequestFactory
from app.views import create_profile
from app.models import Profile, ProfileModel
import sys
# Create your tests here.

# c = Client()
# c.login(username="test", password = "password")
# admin = User.objects.create_superuser('myuser', 'ab1cde@virginia.edu', 'password')


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
            username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.save()

    def test_first_time_login(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 301)
    '''
    def test_existing_signin(self):
        #self.user.id = 10
        response = c.get('/profile')
        response = c.post(('/profile/'), {
            'name': "Test",
            'year': "2020",
            'major': "CS", 
            'bio': "Test data", 
            'skills': "Test data", 
            'courses': "Test data", 
            'organizations': "Test data", 
            'interests': "Test data"})
        #self.assertEqual(response.status_code, 200)
        #response = self.client.get('app/published_profile/10')
        #self.assertEqual(response.status_code, 301)
        #response = self.client.get('profile/')
        self.assertRedirects(response, 'app/published_profile/10')
    '''


c.logout()
User.objects.filter(username=admin.username).delete()
