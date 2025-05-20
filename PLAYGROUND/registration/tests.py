from django.test import TestCase
from.models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        # Create a user instance
        User.objects.create_user(username='testuser', email='email_test', password='testpassword')
        

    def test_profile_creation(self):
        exist = Profile.objects.filter(user__username='testuser').exists()
        # Check if the profile was created successfully
        self.assertEqual(exist, True)
        