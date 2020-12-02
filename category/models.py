from django.db import models
from uuid import uuid4

TYPE_CHOICES = [
    ("INCOME", "INCOME"),
    ("EXPENSE", "EXPENSE")
]

class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    category_title = models.CharField(max_length=255)
    category_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
