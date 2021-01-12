from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realors = Realtor.objects.order_by('-hire_date')
     # get mvp
     
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realors,
        'mvp_realtors':mvp_realtors
    }

    return render(request, 'pages/about.html', context)
