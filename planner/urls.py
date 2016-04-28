from django.conf.urls import url, include
from .views import (
    planner_list,
    planner_create,
    planner_detail,
    planner_update,
    planner_delete
    )

urlpatterns = [
    url(r'^$', planner_list, name='list'),
    url(r'^create/$', planner_create),
    url(r'^(?P<id>\d+)/$', planner_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', planner_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', planner_delete),
]