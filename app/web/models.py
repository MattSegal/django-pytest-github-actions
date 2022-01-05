from django.db import models


class PageViewCount(models.Model):
    title = models.CharField(max_length=32)
    count = models.IntegerField(default=0)
