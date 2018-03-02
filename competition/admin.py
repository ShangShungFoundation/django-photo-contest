# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Competition, Prize, Juror


class PrizeInline(admin.StackedInline):
    model = Prize
    extra = 1
    fieldsets = (
        (None, {
            'fields': (
                ("index", 'name'),
                'description',
                "aworded",
                "observations",
            )
        }),
    )


class JurorInline(admin.StackedInline):
    model = Juror


class CompetitionAdmin(admin.ModelAdmin):
    inlines = [JurorInline, PrizeInline]

    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (
                ("title", 'slug'),
                'summary',
                'description',
                'categories',
                "terms_conditions",
                ("start", "finish"),
                "finals",
                "image",
                "organizer",
            )
        }),
    )


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Prize)
