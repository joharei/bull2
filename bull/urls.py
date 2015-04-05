from django.conf.urls import include, url
from django.contrib import admin
from bull.views import HomePageView

admin.site.site_header = 'Låfteweb-administrasjon'
admin.site.site_title = 'Låfteweb-admin'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^ovingsspeilet/', include('ovingsspeilet.urls', namespace='ovingsspeilet')),
    url(r'^$', HomePageView.as_view(), name='home')
]
