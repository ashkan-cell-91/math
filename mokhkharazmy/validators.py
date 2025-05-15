from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator  

class MaxValueValidator(BaseValidator):  
    def __init__(self, limit_value=None, message=None):  
        super().__init__(limit_value, message or 'Ensure this value is less than or equal to %(limit_value)d.')  
    
    def validate(self, value):  
        if value > self.limit_value:  
            raise ValidationError(self.message, code='max_value', params={'limit_value': self.limit_value})  

    def compare(self, a, b):  
        return a > b  