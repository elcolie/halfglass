from django.db import models
from django.contrib.postgres.fields import JSONField


# http://stackoverflow.com/questions/24403075/django-choicefield
from planner.scheduler_type import SCHEDULER_TYPE, START_TYPE, STOP_TYPE, LIFETIME_UNIT


class Planner(models.Model):
    comment = models.TextField()

    scheduler_type = models.PositiveSmallIntegerField(
        choices=SCHEDULER_TYPE, default=1)
    start_type = models.PositiveSmallIntegerField(
        choices=START_TYPE, default=0)

    start_time = models.TimeField(null=True, blank=True, help_text="start time")
    stop_time = models.TimeField(null=True, blank=True, help_text="stop time")

    month_json = JSONField(null=True, blank=True)    # Jan, Feb, Mar, ...
    weekday_json = JSONField(null=True, blank=True)    # Mon, Tue, Wed, ...
    schedule_days = JSONField(null=True, blank=True)     # 1, 11, 21, 31
    stop_type = models.PositiveSmallIntegerField(null=True, blank=True, choices=STOP_TYPE, default=0)
    lifetime_quantity = models.PositiveSmallIntegerField(null=True, blank=True)
    lifetime_unit = models.PositiveSmallIntegerField(null=True, blank=True, choices=LIFETIME_UNIT, default=0)

    def __str__(self):
        return self.comment