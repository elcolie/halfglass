from django.db import models
from django.contrib.postgres.fields import JSONField


class Planner(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    comment = models.TextField()
    month_day = models.TextField()
    week_day = models.TextField()
    # AttributeError: module
    # 'django.db.models'
    # has
    # no
    # attribute
    # 'JSONField'
    test_json = JSONField()

    def __str__(self):
        return self.name