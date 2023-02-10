from django.db import models
from django_app.models.BaseModel import BaseModel
from django_app.models.ScheduleType import ScheduleType
from django.contrib.auth.models import User
from datetime import datetime


class Record(BaseModel):

    class Status:
        COMPLETED = "COMPLETED"
        EXPIRED = "EXPIRED"
        CREATED = "CREATED"
        ALL = (COMPLETED, EXPIRED, CREATED)
        ALL_DJANGO = ((x, x) for x in ALL)

    schedule_group = models.ForeignKey(ScheduleType,
                                       on_delete=models.PROTECT,
                                       verbose_name='GROUP',
                                       default=ScheduleType.DescriptionList.FAMILY,
                                       )

    holder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', db_index=True)
    description = models.CharField(max_length=200, blank=True, verbose_name='DESCRIPTION')

    status = models.CharField(
        choices=Status.ALL_DJANGO,
        default=Status.CREATED,
        max_length=100,
        verbose_name='STATUS',
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    def __str__(self):
        return f' {self.created.strftime("%Y-%b-%d")} - ' \
               f'{self.holder} - {self.description} - {self.status} - {self.schedule_group}'
