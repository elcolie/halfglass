from django.db import models


class Recurrence(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    comment = models.TextField()
    month_day = models.TextField()
    week_day = models.TextField()

    def __str__(self):
        return self.name

