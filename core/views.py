from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.http.response import HttpResponse

def get_page(request):
    if request.method == "GET":
        return HttpResponse("This is a Anime Recommender site built with django!")
    else:
        return HttpResponse("This is a website")
    
    

# Create your views here.
