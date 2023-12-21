from django.test import SimpleTestCase
from app.calc import add, subtract

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        res = subtract(10, 15)
        self.assertEqual(res, 5)
