from django.db import models
from django.contrib.postgres.fields import JSONField


# http://stackoverflow.com/questions/24403075/django-choicefield
from planner.scheduler_type import SCHEDULER_TYPE, START_TYPE


class Planner(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()

    scheduler_type = models.PositiveSmallIntegerField(
        choices=SCHEDULER_TYPE, default=1)
    start_type = models.PositiveSmallIntegerField(
        choices=START_TYPE, default=0)

    start_time = models.TimeField(null=True, blank=True)
    stop_time = models.TimeField(null=True, blank=True)

    month_json = JSONField(null=True, blank=True)    # Jan, Feb, Mar, ...
    weekday_json = JSONField(null=True, blank=True)    # Mon, Tue, Wed, ...
    date_json = JSONField(null=True, blank=True)     # 1, 11, 21, 31

    def __str__(self):
        return self.name