from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address')
    owner = models.IntegerField("venue owner", blank=False, default=1) #we dont use the deafult in real world (just for testing venues already created cause blank is false admin 1 so default)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')


    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE) #with this foreing key we ration tables together (ON DELETE DELETES THE OTHER CONNECT FIELDS OF TABLES IF WE DELETE)
   # venue = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) #set_null if we delete manager it doesnt delet events (tables connected)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True) #this connects user with htis table (connects user to many posibilities)


    def __str__(self):
        return self.name
