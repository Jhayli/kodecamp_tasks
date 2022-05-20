from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    return HttpResponse('<p> Signup here </p>')

def login(request):
    return HttpResponse('<b> Login here </b>')

def checkout(request):
    return HttpResponse('<p> Checkout </p>')


