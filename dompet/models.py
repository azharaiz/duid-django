import uuid

from django.db import models

# Create your models here.
from authentication.models import User

class Dompet(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                  editable=False)
    account_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
