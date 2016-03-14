from django.shortcuts import render, get_object_or_404
# Need to import HttpResponse 
from django.http.response import HttpResponse
from django.http import JsonResponse

import json

from .models import Question, Choice

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

def sarah_page(request):

    return render(request, 'poll_site/sarah.html')

def question_details(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question, 
    }

    return render(request, 'poll_site/question_details.html', context)

def submit_vote(request):
    """ Handles vote submissions via AJAX """

    if request.method == 'POST':

        #Decode request body from bytecode to normal 
        data_json = request.body.decode('utf-8')

        #convert data from string to object 
        data = json.loads(data_json)
        
        #Get the choice at that id 
        choice = Choice.objects.get(pk=int(data['choice_id']))

        #increments the votes of the choice by 1 
        choice.votes += 1

        #Save the updates object coice ot the database 
        choice.save()

        #Get all the choices for the question just voted on 
        question = Question.objects.get(pk=int(data['question_id']))
        #This will give us all the choices for the question 
        question_choices = question.choice_set.all()


        #build the response data 
        response = []

        #loop through the choices and add them to a dictonary 
        for choice in question_choices:
            c_dict = {
                'id': choice.id, 
                'text':choice.choice_text, 
                'votes': choice.votes
            }
            response.append(c_dict) 

        # #turns python to json 
        # response_json = json.dumps(response)

    #built in - takes a python which it turns into a JSON string 
    return JsonResponse({'data':response})


