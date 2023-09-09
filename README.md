# AlphaDTech
Medihacks prj

<h3>For the frontend guys:</h3>
<h6>(assuming youve never used Django)<h6>
<p>You really dont need to focus on anything but the /static folders there you can see the css, js, and images for the frontend 
    The html will be in the templates folder you can create subfolders in that for better organization<p>
    <br></br>
    <h6>You may notice that the html files have these lines:</h6>
    
```html
{% block content %}
{% load static %}
{% csrf_token %}

{% endblock %}
```
<p>as you probably geussed these are needed</p>


```python
#views.py:
def home(request):
    global num #ignore
    return render(request, 'home.html', {'num': num,})
```
```python
#urls.py:
from django.contrib import admin
from django.urls import path
from .views import home, update_num
urlpatterns = [
     path('', home, name='home'),
     path('update-num', update_num, name='update-num'),
]
```
<p>inside views.py this is how a page is rendered, anytime you create an html file you would need to include this. However in reality I and the other backend guy should be able to that</p>

<p>Otherwise just make normal static pages and we should be able to integrate it properly. Ignore the num, that was simply used for a demonstration of how one might communicate with the backend</p>
<h1>INSTALL</h1>
<h6>When I created the requirments.txt I was not in a venv meaning if you do install that way than you will be installing every package I've ever installed, I think all you should need is Django, and python, which their installs are simple I think<h6>

    
    