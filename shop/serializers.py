from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True) 
    price_rwf = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'price', 'price_rwf']

    def get_price_rwf(self, obj):
        return f"RWF {int(obj.price):,}"
