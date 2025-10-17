from django.test import SimpleTestCase

class SimpleMathTest(SimpleTestCase):
    def test_basic_addition(self):
        """Basic math test to check CI works."""
        self.assertEqual(2 + 2, 4)
