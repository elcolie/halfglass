from django.conf.urls import url, include
from .views import (
    scheduler_list,
    scheduler_create,
    scheduler_detail,
    scheduler_update,
    scheduler_delete
    )

urlpatterns = [
    url(r'^$', scheduler_list, name='list'),
    url(r'^create/$', scheduler_create),
    url(r'^(?P<id>\d+)/$', scheduler_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', scheduler_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', scheduler_delete),
]
