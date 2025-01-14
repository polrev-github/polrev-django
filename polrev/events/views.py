from django.shortcuts import render
from django.http import JsonResponse
from .models import Event
from .utils.heatmap import generate_heatmap

def calendar(request):
    return render(request, 'events/calendar.html')

def api_events(request):
    data = [
      {
        "title": "Code for Denver Monthly",
        "url": "https://www.meetup.com/codefordenver/",
        'rrule': {
          'freq': 'monthly',
          'byweekday': [ 'sa' ],
          'bysetpos': [3],
          'dtstart': '2019-04-20T13:00:00',
        },

        # for specifying the end time of each instance
        'duration': '02:00'
      },
      {
        "title": "Christmas",
        "className": "fc-holiday",
        "start": "2019-12-25"
      },
      {
        "title": "Spring",
        "className": "fc-holiday",
        "start": "2019-03-20"
      },
      {
        "title": "Summer",
        "className": "fc-holiday",
        "start": "2019-06-21"
      },
      {
        "title": "Independence Day",
        "className": "fc-holiday",
        "start": "2019-07-04"
      }
    ]

    return JsonResponse(data, safe=False)

def event_heatmap(request):
    events = Event.objects.all()
    heatmap_path = generate_heatmap(events)
    return render(request, 'events/heatmap.html', {'heatmap_path': heatmap_path})
