from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.contrib.auth.models import User

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)


	def __str__(self):
		return f'{self.first_name} {self.last_name} {self.phone} {self.password}'

  

class Product(models.Model):  
    name = models.CharField(max_length=100)  # نام فارسی  
    en_name = models.CharField(max_length=100, default='', blank=True)  # نام انگلیسی  
    picture = models.ImageField(upload_to='uploads/product/', blank=True, null=True)  # تصویر محصول  

    def upload_to(instance, filename):
        return f'products/{instance.name}/{filename}'

    def __str__(self):
        return self.name

class PointsValidator(BaseValidator):  
    def __init__(self, limit_value=None, message=None):  
        super().__init__(limit_value, message)  

    def __call__(self, value):  
        if not isinstance(value, list):  
            raise ValidationError('نقاط باید به صورت لیست ارسال شوند')  
        
        for point in value:  
            if len(point) != 2:  
                raise ValidationError('هر نقطه باید دقیقاً دارای ۲ مختصات باشد')  
            
            try:  
                x, y = map(float, point)  
            except (TypeError, ValueError):  
                raise ValidationError('مختصات باید مقادیر عددی باشند')   


class Calculation(models.Model):  
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  
    shape_type = models.CharField(max_length=50)  # یا هر نوع فیلد که مناسب است  
    points = models.JSONField(  
        verbose_name='مختصات نقاط',  
        validators=[PointsValidator()]  
    )  
    perimeter = models.FloatField(null=True, blank=True)  
    area = models.FloatField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  # اضافه کردن فیلد  

    def clean(self):
        """اعتبارسنجی تعداد نقاط"""
        shape_point_map = {
            'triangle': 3,
            'quadrilateral': 4,
            'pentagon': 5,
            'hexagon': 6  # اضافه شده
        }
        
        required_points = shape_point_map.get(self.shape_type)
        if required_points and len(self.points) != required_points:
            raise ValidationError(
                {'points': f'برای {self.get_shape_type_display()} باید دقیقاً {required_points} نقطه وارد کنید'}
            )
        




    
    