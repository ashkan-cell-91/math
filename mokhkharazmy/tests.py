from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Calculation
from django.core.exceptions import ValidationError

User = get_user_model()

class CalculationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')

    def test_valid_calculation(self):
        calc = Calculation(
            user=self.user,
            shape_type='triangle',
            points=[[0,0], [4,0], [2,3]],
            perimeter=9.0,
            area=6.0
        )
        calc.full_clean()  # نباید خطا بدهد
        calc.save()
        self.assertEqual(Calculation.objects.count(), 1)

    def test_invalid_points(self):
        with self.assertRaises(ValidationError):
            calc = Calculation(
                user=self.user,
                shape_type='triangle',
                points=[[0,0], [1,1]],  # فقط ۲ نقطه
                perimeter=0,
                area=0
            )
            calc.full_clean()