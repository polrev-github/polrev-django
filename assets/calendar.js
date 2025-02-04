/*import { FullCalendarModule } from "@fullcalendar/angular";
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';
import listPlugin from '@fullcalendar/list';
import momentPlugin from '@fullcalendar/moment';
import rrulePlugin from '@fullcalendar/rrule';
import timeGridPlugin from '@fullcalendar/timegrid';

FullCalendarModule.registerPlugins([
  dayGridPlugin,
  interactionPlugin,
  listPlugin,
  momentPlugin,
  rrulePlugin,
  timeGridPlugin
]);*/

import { Calendar } from '@fullcalendar/core';

import rrulePlugin from '@fullcalendar/rrule';
import dayGridPlugin from '@fullcalendar/daygrid';

import './scss/calendar.scss'

document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');

  const calendar = new Calendar(calendarEl, {
    events: '/events/api/events',
    plugins: [ rrulePlugin, dayGridPlugin ],
    initialView: 'dayGridMonth'
  });
  
  calendar.render();
});