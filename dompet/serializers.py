from rest_framework import serializers

from authentication.models import User
from .models import Dompet


class DompetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


    class Meta:
        model = Dompet
        fields = ('account_id', 'account_title', 'created_at', 'updated_at', 'user')
