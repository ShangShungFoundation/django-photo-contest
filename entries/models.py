# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

from authors.models import Author


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 0.5
    #import ipdb; ipdb.set_trace()
    if filesize < megabyte_limit * 1024 * 1024:
        raise ValidationError("Min image file size is %sMB" % str(megabyte_limit))


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
    image = models.ImageField(upload_to='entries', validators=[validate_image])
    category = models.CharField(max_length=20)
    metadata = models.TextField(blank=True, null=True)
    submited_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'entries'

    def __str__(self):
        return "%s %s %s" % (self.id, self.author.email, self.title)
