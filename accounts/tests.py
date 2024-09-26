from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()

class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@gmail.com',
            password='password',
            first_name='Test',
            last_name='User'
        )

    def test_user_creation(self):
        """Test creating a new user"""
        self.assertEqual(self.user.email, 'testuser@gmail.com')
        self.assertTrue(self.user.check_password('password'))
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)

    def test_user_str(self):
        """Test the string representation of the user"""
        self.assertEqual(str(self.user), 'testuser@gmail.com')

    def test_user_bmi(self):
        """Test the BMI property of the user"""
        self.user.weight = 70  #kg
        self.user.height = 175  #cm
        self.assertEqual(self.user.bmi, round(70 / (1.75 ** 2), 2))

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@gmail.com',
            password='password'
        )

    def test_login(self):
        """Test user login"""
        response = self.client.login(email='testuser@gmail.com', password='password')
        self.assertTrue(response)

    def test_login_invalid(self):
        """Test login with invalid credentials"""
        response = self.client.login(email='wronguser@gmail.com', password='wrongpassword')
        self.assertFalse(response)

