import uuid
from datetime import datetime

from django.db import models
from rest_framework.exceptions import ValidationError

from authentication.models import User
from target.util import monthly_deposit_calculator


class Target(models.Model):
    target_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    target_title = models.CharField(max_length=100)
    target_amount = models.PositiveBigIntegerField()
    annual_invest_rate = models.FloatField(default=0)
    monthly_deposit_amount = models.PositiveBigIntegerField(default=0)

    def clean(self):
        due_date_year = int(
            str(self.due_date).split('-')[0]) - int(datetime.now().year)

        self.monthly_deposit_amount = \
            monthly_deposit_calculator(0,
                                       self.annual_invest_rate,
                                       due_date_year,
                                       self.target_amount)

        rate_error_msg = 'annual_invest_rate cant be negative value'
        if self.annual_invest_rate < 0:
            raise ValidationError({'annual_invest_rate': rate_error_msg})

        if self.target_amount <= 0:
            raise ValidationError(
                {'target_amount': 'target amount must be more than 0'})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)
