from django.core.validators import BaseValidator  

class MyValidator(BaseValidator):  
    def __init__(self, limit_value, message=None):  
        super().__init__(limit_value, message)  # ensure limit_value is passed  