from __future__ import unicode_literals

from django.db import models


FILE_CATEGORIES = (
    (0, 'Introduction'),
    (1, 'Presentation'),
    (2, 'Team Presentation'),
    (3, 'Conclusion')
)

class Company(models.Model):
    class Meta:
        db_table = 'company'
        app_label = 'bricks'

    name = models.CharField(max_length=255)


class BricksUser(models.Model):
    class Meta:
        db_table = 'bricks_user'
        app_label = 'bricks'

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class SlideSlice(models.Model):
    class Meta:
        db_table = 'slide_slice'
        app_label = 'bricks'

    name = models.CharField(max_length=255, blank=False)
    start = models.IntegerField(blank=False)
    count = models.IntegerField(blank=False)
    remote_path = models.CharField(max_length=255, blank=False)
    category = models.CharField(choices=FILE_CATEGORIES, max_length=255, blank=False)
    user = models.ForeignKey(BricksUser, on_delete=models.CASCADE)
