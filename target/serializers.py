from rest_framework import serializers

from authentication.models import User
from target.models import Target


class TargetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Target
        fields = (
            'target_id', 'user', 'due_date', 'target_title', 'target_amount',
            'annual_invest_rate', 'monthly_deposit_amount')
