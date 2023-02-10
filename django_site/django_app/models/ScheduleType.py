from django.db import models
from django_app.models.BaseModel import BaseModel


class ScheduleType(BaseModel):

    class DescriptionList:
        FAMILY = "FAMILY"
        INDIVIDUAL = "INDIVIDUAL"
        ALL_DJANGO = ((x, x) for x in (FAMILY, INDIVIDUAL))

    description = models.CharField(
        choices=DescriptionList.ALL_DJANGO,
        default=DescriptionList.FAMILY,
        max_length=100,
        verbose_name='BELONG TO',
        unique=True,
    )

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Group'

    def __str__(self):
        return f' {self.description}'
