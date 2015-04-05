from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from ovingsspeilet import views

urlpatterns = [
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^$', login_required(TemplateView.as_view(template_name="ovingsspeilet/rehearsal.html")), name='rehearsal'),
]