from cProfile import label
from tkinter import Widget
from django import forms
from django.forms import ModelForm, SelectMultiple
from .models import Venue, Event

#admin super user event form
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event 
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')

        labels = {
            'name': '',
            'event_date': 'YYY-MMM-DD HH:MM:SS',
            'venue':'venue',
            'manager': 'manager',
            'description': '',
            'attendees':'attendees',

        }


#style bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'event name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'event date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'venue'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'manager'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'description'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'attendees'}),
        }


#usereventform
class EventForm(ModelForm):
    class Meta:
        model = Event 
        fields = ('name', 'event_date', 'venue', 'description', 'attendees')

        labels = {
            'name': '',
            'event_date': 'YYY-MMM-DD HH:MM:SS',
            'venue':'venue',
            'description': '',
            'attendees':'attendees',

        }


#style bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'event name'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'event date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'venue'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'description'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'attendees'}),
        }








class VenueForm(ModelForm):
    class Meta:
        model = Venue 
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address', "venue_image")

        labels = {
            'name': '',
            'address': '',
            'zip_code':'',
            'phone': '',
            'web': '',
            'email_address':'',
            'venue_image':'',

        }


#style bootstrap
        widgets = {
            'name': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'venue name'}),
            'address': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'address'}),
            'zip_code': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'zip code'}),
            'phone': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'phone'}),
            'web': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'website'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),
        }