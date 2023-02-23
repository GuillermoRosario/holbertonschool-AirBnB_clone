import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test for class User"""

    def test_email(self):
        """Test class attributes named email"""
        obj = User()
        self.assertEqual(obj.email, "")
        obj.email = "testingtesting"
        self.assertEqual(obj.email, "testingtesting")

    def test_password(self):
        """Test class attributes named password"""
        obj = User()
        self.assertEqual(obj.password, "")
        obj.password = "testingtesting"
        self.assertEqual(obj.password, "testingtesting")

    def test_first_name(self):
        """Test class attributes named first name"""
        obj = User()
        self.assertEqual(obj.first_name, "")
        obj.first_name = "testingtesting"
        self.assertEqual(obj.first_name, "testingtesting")

    def test_last_name(self):
        """Test class attributes named last name"""
        obj = User()
        self.assertEqual(obj.last_name, "")
        obj.last_name = "testingtesting"
        self.assertEqual(obj.last_name, "testingtesting")


if __name__ == '__main__':
    unittest.main()
