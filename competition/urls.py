from django.conf.urls import url

from .views import contest

urlpatterns = [
    url(r'^(?P<slug>.+)/$',
        contest, name='contest'),
]
