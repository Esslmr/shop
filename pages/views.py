from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from builders.models import Builder
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    builders = Builder.objects.all()
    mvp_builders = Builder.objects.all().filter(is_mvp=True)

    context = {
        'builders': builders,
        'mvp_builders': mvp_builders
    }

    return render(request, 'pages/about.html', context)
