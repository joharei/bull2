from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from ovingsspeilet.models import Event


@login_required
def calendar(request):
    event_objects = Event.objects.all()
    events = []
    for event in event_objects:
        events.append({
            'id': event.id,
            'title': event.title,
            'start': timezone.localtime(event.date_start),
            'end': timezone.localtime(event.date_end)
        })
    return JsonResponse(events, safe=False)