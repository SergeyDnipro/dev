from django.db import models
import uuid


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    id = models.UUIDField(default=uuid.uuid4())

    class Meta:
        abstract = True