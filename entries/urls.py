from django.conf.urls import url

from .views import submit_entry

urlpatterns = [
    url(r'^(?P<slug>.+)/(?P<email>.+)$',
        submit_entry, name='submit_entry'),
]
