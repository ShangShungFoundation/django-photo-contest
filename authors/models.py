from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    """docstring for Entry"""
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    country = models.CharField(max_length=4)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
