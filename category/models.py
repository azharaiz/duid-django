from uuid import uuid4
from django.db import models
from authentication.models import User

TYPE_CHOICES = [
    ("INCOME", "INCOME"),
    ("EXPENSE", "EXPENSE")
]


class Category(models.Model):
    category_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=255)
    category_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "category_title"],
                name="user_title_unique_together")
        ]
