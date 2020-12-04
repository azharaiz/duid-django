from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'