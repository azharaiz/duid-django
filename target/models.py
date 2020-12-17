import uuid

from django.db import models

from authentication.models import User


# Create your models here.


class Target(models.Model):
    target_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    target_title = models.CharField(max_length=100)
    target_amount = models.PositiveBigIntegerField()
