import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test for class Review"""

    def test_place_id(self):
        """Test class attributes named place id"""
        obj = Review()
        self.assertEqual(obj.place_id, "")
        obj.place_id = "testingtesting"
        self.assertEqual(obj.place_id, "testingtesting")

    def test_user_id(self):
        """Test class attributes named user id"""
        obj = Review()
        self.assertEqual(obj.user_id, "")
        obj.user_id = "testingtesting"
        self.assertEqual(obj.user_id, "testingtesting")

    def test_text(self):
        """Test class attributes named text"""
        obj = Review()
        self.assertEqual(obj.text, "")
        obj.text = "testingtesting"
        self.assertEqual(obj.text, "testingtesting")


if __name__ == '__main__':
    unittest.main()
