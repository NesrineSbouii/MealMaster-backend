from django.shortcuts import render
from django.template import context

from .models import MonImage
from django.http import HttpResponse

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_images= MonImage.objects.all().count()
    return HttpResponse('<h1 style="color:red">Welcom to MASTER Meal !</h1>' )

    # Render the HTML template index.html with the data in the context variable.
    #return render(request, 'MealMaster_App/templates/index.html', context)

