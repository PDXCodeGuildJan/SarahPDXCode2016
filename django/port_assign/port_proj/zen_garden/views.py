from django.shortcuts import render

#We added this to handle the HttpResponse in this particular manner.
from django.http.response import HttpResponse

# Create your views here.

def render_zen_garden(request):
    return render(request, 'zen_garden/zen_mockup.html')

