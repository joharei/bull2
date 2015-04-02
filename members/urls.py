from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from members.models import Member, Group

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Member), name='detail'),
    url(r'^$', ListView.as_view(model=Member), name='list'),
    url(r'^groups/$', ListView.as_view(model=Group), name='group-list'),
    url(r'^groups/(?P<pk>\d+)/$', DetailView.as_view(model=Group), name='group-detail'),
]
