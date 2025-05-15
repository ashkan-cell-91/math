from rest_framework import serializers
from .models import Calculation

class CalculationSerializer(serializers.ModelSerializer):
    points = serializers.ListField(
        child=serializers.ListField(
            child=serializers.FloatField(),
            min_length=2,
            max_length=2
        ),
        write_only=True
    )

    class Meta:
        model = Calculation
        fields = ['id', 'user', 'shape_type', 'points', 'perimeter', 'area', 'created_at']
        read_only_fields = ['id', 'user', 'perimeter', 'area', 'created_at']

    def validate_points(self, value):
        if not value:
            raise serializers.ValidationError("لیست نقاط نمی‌تواند خالی باشد")
        return value

    def validate(self, data):
        points = data.get('points', [])
        shape_type = data.get('shape_type')
        
        shape_point_map = {
            'triangle': 3,
            'quadrilateral': 4,
            'pentagon': 5,
            'hexagon': 6
        }
        
        if shape_type in shape_point_map and len(points) != shape_point_map[shape_type]:
            raise serializers.ValidationError({
                'points': f"برای شکل {shape_type} باید دقیقاً {shape_point_map[shape_type]} نقطه وارد کنید"
            })
        
        return data