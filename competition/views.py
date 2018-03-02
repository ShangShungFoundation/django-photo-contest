from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from .models import Competition

from authors.forms import AuthorForm


def contest(request, slug):
    contest = Competition.objects.get(slug=slug)
    author = None
    author_form = AuthorForm(request.POST or None)

    if author_form.is_valid():
        author = author_form.save()
        return redirect('submit_entry', slug=contest.slug, email=author.email)

    return render(
        request, "contest/contest.html",
        dict(contest=contest, author_form=author_form))
