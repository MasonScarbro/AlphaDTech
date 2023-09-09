from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
num = 1
def home(request):
    global num
    return render(request, 'home.html', {'num': num,})

def update_num(request):
    global num
    if request.method == 'POST':
        num = num + 1
        response_data = {'num': num}
        return JsonResponse(response_data)