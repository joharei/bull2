from django.contrib import admin
from django.db import models
from bull.config import settings


class Event(models.Model):
    title = models.CharField(max_length=40, verbose_name='tittel')
    description = models.TextField(max_length=10000, blank=True, verbose_name='beskrivelse')
    created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateField(verbose_name='starttidspunkt')
    date_end = models.DateField(verbose_name='sluttidspunkt')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='opprettet av')
    weekly = models.BooleanField(default=False, verbose_name='ukentlig', help_text='Repeter ukentlig.')
    admin_event = models.BooleanField(default=False, verbose_name='adminaktivitet',
                                      help_text='Kan kun endres av en admin.')

    def __unicode__(self):
        if self.title:
            return self.creator + " - " + self.title
        else:
            return self.creator + " - " + self.snippet[:40]

    def short(self):
        if self.description:
            return "<i>%s</i> - %s" % (self.title, self.description)
        else:
            return self.title

    short.allow_tags = True

    class Meta:
        verbose_name = 'aktivitet'
        verbose_name_plural = 'aktiviteter'


class EventAdmin(admin.ModelAdmin):
    list_display = ["creator", "date_start", "title", "description"]
    list_filter = ["creator"]


admin.site.register(Event, EventAdmin)