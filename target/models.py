import uuid

from django.db import models
from rest_framework.exceptions import ValidationError

from authentication.models import User


class Target(models.Model):
    target_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                 editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    target_title = models.CharField(max_length=100)
    target_amount = models.PositiveBigIntegerField()

    def clean(self):
        if self.target_amount <= 0:
            raise ValidationError(
                {'target_amount': 'target amount must be more than 0'})

    def save(self, *args, **kwargs):
        self.clean()
        return super(Target, self).save(*args, **kwargs)
