# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from authors.models import Author


class Entry(models.Model):
    competition = models.ForeignKey(
        'competition.Competition',
        on_delete=False,
        related_name="related_entries")
    author = models.ForeignKey(
        Author,
        on_delete=False,
        related_name="related_entries")
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length=20)
    metadata = models.TextField(blank=True, null=True)
    submited_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'entries'

    def __str__(self):
        return "%s %s %s" % (self.id, self.author.email, self.title)
