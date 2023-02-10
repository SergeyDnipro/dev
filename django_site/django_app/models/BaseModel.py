from django.db import models
import uuid
from datetime import datetime


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True
