from django.shortcuts import render
from django.http import HttpResponse
from newapp.models import Customer
from .forms import CustomerForm

#Create your views here.
def addnew (request):

    formentry = CustomerForm()
    
    return render(request, 'addnew.html', {"formentry": formentry})

def home (request):

    x = Customer.objects.all()

    return render(request, 'index.html', { "data" : x})





