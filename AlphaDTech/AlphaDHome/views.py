from django.http import JsonResponse
from django.shortcuts import render
import openai
from decouple import config
import requests
import re

openai_api_key = config('OPENAI_API_KEY')
openai.api_key = openai_api_key

global response_string 

# Potentially a new openAI instance that will handle the JSON from the AlphaFold API so that we can return a description of the protein


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You are an expert on Protein folds and you are well versed about the UniProtKB and AlphaFold database, given a disease you can return a potential protein associated with it, with that you will respond with the proper AlphaFold accession number surrounded in brackets only the accension numbers should be wrapped in brackets!, YOU WILL ONLY GIVE AN ACCENSION NUMBER IF IT HAS A pdb file associated with it !THIS IS IMPORTANT! If You do not think it has an accension number with it provide a random accesnion number that does"}, #Better Prompt this
            {"role": "user", "content": message}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.



def home(request):
    pdbUrl_response = []
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message) #makes response the chatGPT response
        
        global response_string 
        pdbUrl_response = re.findall(r'\[(.*?)\]', response);
        #Regex this based on prompt to only be the UkprotKit orr wtvr

        return JsonResponse({'message': message, 'response': response, 'pdbUrl_response': pdbUrl_response})
    return render(request, 'home.html')