from django.conf.urls import url
from django.views.generic import TemplateView
from ovingsspeilet import views

urlpatterns = [
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^$', TemplateView.as_view(template_name="ovingsspeilet/rehearsal.html"), name='rehearsal'),
]