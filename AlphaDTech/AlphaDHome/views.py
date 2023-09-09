from django.http import JsonResponse
from django.shortcuts import render
import openai
from decouple import config

openai_api_key = config('OPENAI_API_KEY')
openai.api_key = openai_api_key

global response_string 

# Potentially a new openAI instance that will handle the JSON from the AlphaFold API so that we can return a description of the protein


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You are a Helpful Assistant and Tutor"}, #Better Prompt this
            {"role": "user", "content": message}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.

# Api function that returns the Json response here
'''
#Insert Implementation Here
'''
def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message) #makes response the chatGPT response
        
        global response_string 
        response_string = response
        #Regex this based on prompt to only be the UkprotKit orr wtvr

        return JsonResponse(
            {
            'message': message, 
            'response': response,
            #'AlphaResponse': AlphaResponse, 
            })
    return render(request, 'home.html')