from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Announcement

def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'bands': bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listing(request):
    announcements = Announcement.objects.all()
    return render(request,
           'listings/listing.html',
           {'announcements': announcements})

def contact_us(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Veuillez nous contacter <a href="">ici</a> !</p>')

