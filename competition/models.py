# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from djrichtextfield.models import RichTextField

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from entries.models import Entry


class Competition(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    summary = models.TextField()
    image = models.ImageField()
    categories = models.TextField()
    description = RichTextField()
    terms_conditions = RichTextField()

    start = models.DateField()
    finish = models.DateField()
    finals = models.DateField()

    organizer = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)

    def is_open(self):
        now = timezone.now()
        return now > self.start and now < self.finish

    def has_finals(self):
        now = timezone.now()
        return now > self.finals

    @property
    def categories_list(self):
        return self.categories.split(', ')

    def __str__(self):
        return "%s %s" % (self.finals, self.title)


class Prize(models.Model):
    competition = models.ForeignKey(
        Competition,
        on_delete=False,
        related_name="related_prizes")

    index = models.IntegerField()
    name = models.CharField(max_length=250)
    description = models.TextField(
        blank=True, null=True)

    aworded = models.ManyToManyField(
        Entry, blank=True,
        related_name="related_awords")
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.name


class Juror(models.Model):
    competition = models.ForeignKey(
        Competition,
        on_delete=False,
        related_name="jurors")
    user = models.ForeignKey(
        User,
        on_delete=False,
        related_name="related_jurors")
    role = models.CharField(max_length=250)