from django.shortcuts import render
from django.http.response import HttpResponse 

# Create your views here.

def render_price_list(request):
    # return HttpResponse("Does this work?")
    return render(request, 'price_list/pricing.html')
