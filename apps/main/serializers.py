# DRF
from rest_framework import serializers

# Local
from .models import Car

class CarsSerializer(serializers.ModelSerializer):
    """CarsSerializer."""
    brand = serializers.CharField
    model = serializers.CharField
    horsepower = serializers.IntegerField
    price = serializers.FloatField
    owner = serializers.SerializerMethodField(
        method_name='get_owner'
    )

    class Meta:
        model = Car
        fields = (
            'brand',
            'model',
            'horsepower',
            'owner',
            'price'
        )

    def get_owner(self,obj:Car) -> str:
        return f"{obj.owner}"