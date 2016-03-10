from django.shortcuts import render

# Need to import HttpResponse 
from django.http.response import HttpResponse

# Create your views here.

def hello_world(request): 
#make the function that alludes to what pages it is going to 
#Has to take one parameter into it, request - HTTP by default 

    #Always need to return an HTTPResponse 
    return HttpResponse("Hello World") 

def hello_world_render(request):

    context = {
        'name': "Sarah", 
        'fav_color': "Yellow",
        'toys': [
            'snowboard', 
            'tennis racket', 
            'yoga mat', 
            'kick ball'
        ]
    }

    #return an HttpResponse object, using the render function 
    #render is a build in object - takes a requst object and a template name (relative path). 
        #return an Httpresponce
    return render(request, 'poll_site/index.html', context)