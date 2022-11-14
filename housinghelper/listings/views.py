from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Listing
from .forms import ListingForm, TestForm
from django.shortcuts import render, redirect

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/index.html', context)


def listing(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def createlisting(request):
    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/listing_form.html', context)
    
def browselisting(request):
    
    all_listings=Listing.objects.all

    return render(request, 'listings/browse_houses.html', {'all':all_listings})
   

def deletelisting(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')

#Factory method
def updatelisting(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance = listing)
    check(request, pk)
    context = {
    'form' : form
    }
    return render(request, 'listings/updatelisting.html', context)


    
def check(request, pk):
    if request.method == 'POST':
        listing = Listing.objects.get(id=pk)
        form = ListingForm(request.POST, instance = listing)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            listing = Listing.objects.get(id=pk)
            form = ListingForm(instance = listing)
            return form


def calcmortgage(request):
    form = TestForm()
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return redirect('/')
    context = {'form': form}
    return render(request, 'listings/calc_form.html', context)
