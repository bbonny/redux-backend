from __future__ import unicode_literals

from django.db import models


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


class Brick(models.Model):
    class Meta:
        db_table = 'brick'
        app_label = 'bricks'

    name = models.CharField(max_length=255, blank=False)
    start = models.IntegerField(blank=False)
    count = models.IntegerField(blank=False)
    remote_path = models.CharField(max_length=255, blank=False)
    column = models.IntegerField()
    checked = models.BooleanField()
