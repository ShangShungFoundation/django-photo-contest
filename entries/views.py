from __future__ import unicode_literals

from django.shortcuts import render

from competition.models import Competition
from authors.models import Author

from .forms import EntryForm


def submit_entry(request, slug, email):
    competition = Competition.objects.get(slug=slug)
    author = Author.objects.get(email=email)
    entry = None
    msg = ""

    entry_form = EntryForm(
        request.POST or None, request.FILES or None,
        initial={'author': author, 'competition': competition})

    # import ipdb; ipdb.set_trace()
    if entry_form.is_valid():
        entry = entry_form.save()
        msg = "Thank You! Your photo has been uploaded successfully. You may submit another one"

    return render(
        request, "entry/entry.html",
        dict(
            entry_form=entry_form,
            author=author,
            contest=competition, msg=msg))
