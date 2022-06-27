from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar
from datetime import date, datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User


#with events we have one way to connect things to database using foreing key connected to django deafult user model

#with venues we have another way to connect things to database usign owner id in models connected to django default user 

def search_events(request):
    if request.method == "POST":
        searched = request.POST['searched']
        events = Event.objects.filter(name__contains=searched)

        return render(request, 'eventsapp/search_events.html', {'searched': searched, 'events': events})
    else:
        return render(request, 'eventsapp/search_events.html', {})



def my_events(request):              ###this is the profileeee code
    if request.user.is_authenticated:
        me = request.user.id
        events = Event.objects.filter(manager = me)



        return render(request, 'eventsapp/my_events.html', {'events':events} )

    else:
         messages.success(request, 'no access to this bitch!') 
         return redirect('login')





# download excel files
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'
    writer = csv.writer(response)
    venues = Venue.objects.all()
    writer.writerow(['venue name', 'address', 'zip code', 'email'])
    for venue in venues:
        writer.writerow([venue.name, venue.address])
    return response




#download files (data from mdatabase)
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    venues = Venue.objects.all()
    lines=[]
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n')
    #lines = ["line one", "seconde line"]
    response.writelines(lines)
    return response





def delete_venue(request, venue_id):
        event = Venue.objects.get(pk=venue_id)
        event.delete()
        return redirect('list-venues')



def delete_event(request, event_id):
        event = Event.objects.get(pk=event_id)
        if request.user == event.manager:
           event.delete()
           messages.success(request, 'Event deleted!')
           return redirect('list-events')
        else:
           messages.success(request, 'no access to this bitch!') 
           return redirect('list-events')





def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'eventsapp/update_event.html', {'event': event, 'form': form})

 



def add_event(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
           form = EventFormAdmin(request.POST)
           if form.is_valid():                                            
                   form.save()
                   return HttpResponseRedirect('/add_event?submitted=True')
        else:
           form = EventForm(request.POST)
           
           if form.is_valid():                                              #if they filled up the form
              event = form.save(commit=False)  
              event.manager = request.user   #we we are connecting logged in user (model) with our model event manager field                               
              event.save()
              return HttpResponseRedirect('/add_event?submitted=True')    

    else:
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'eventsapp/add_event.html', {'form': form, 'submitted':submitted})





def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'eventsapp/update_venue.html', {'venue': venue, 'form': form})







def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)

        return render(request, 'eventsapp/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'eventsapp/search_venues.html', {})





#grab specific venue by id (id is created automatically in database models)
def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue_owner = User.objects.get(pk=venue.owner)
    return render(request, 'eventsapp/show_venue.html', {'venue': venue, 'venue_owner': venue_owner})




def list_venues(request):
    venue_list = Venue.objects.all().order_by('name') # ? to order them randomly

    #pagination 
    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    

    return render(request, 'eventsapp/venue.html', {'venue_list': venue_list, 'venues': venues})



def add_venue(request):
    submitted = False
    if request.method == "POST":
      form = VenueForm(request.POST, request.FILES) #files for uploading images
      if form.is_valid():
          venue = form.save(commit=False)  
          venue.owner = request.user.id                                
          venue.save()
          return HttpResponseRedirect('/add_venue?submitted=True')    

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'eventsapp/add_venue.html', {'form': form, 'submitted':submitted})





def all_events(request):
    event_list = Event.objects.all().order_by('-event_date')
    return render(request, 'eventsapp/event_list.html', {'event_list': event_list})





def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'jhon'
    month = month.capitalize()

    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M %p')
    return render(request, 'eventsapp/home.html', {"name": name, "year": year, "month": month, "month_number": month_number, "cal": cal, "current_year": current_year, "time":time})