from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
def listing(request):
    return HttpResponse('<h1>Listings</h1> <p>Liste complète</p>')

def contact_us(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Veuillez nous contacter <a href="">ici</a> !</p>')

