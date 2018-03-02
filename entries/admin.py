# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'author',
                'title',
                'description',
                'image',
                'category',
                'metadata',
            )
        }),
    )

    def formfield_for_choice_field(self, db_field, request, **kwargs):
            if db_field.name == "category":
                kwargs['choices'] = (
                    ('accepted', 'Accepted'),
                    ('denied', 'Denied'),
                )

            return super(EntryAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)


admin.site.register(Entry, EntryAdmin)