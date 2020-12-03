from rest_framework import serializers
from .models import Dompet


class DompetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dompet
        fields = ('account_id', 'account_title', 'created_at', 'updated_at')