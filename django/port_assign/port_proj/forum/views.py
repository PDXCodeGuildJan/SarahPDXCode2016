from django.shortcuts import render
from django.http.response import HttpResponse 

# Create your views here.
def render_forum(request):
    return render(request, 'forum/forum.html')





    