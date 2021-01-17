import uuid
from django.db import models

from authentication.models import User
from dompet.models import Dompet
from category.models import Category


class Transaction(models.Model):
    transaction_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dompet = models.ForeignKey(Dompet, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
