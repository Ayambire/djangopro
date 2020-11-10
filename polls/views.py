from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Hello,world! This is my first application at Aiti-Kace <br> I am professional data analyst from Aiti-Kace<h1/>"
                        "<p> The institution is next to non when it comes to hands on desk programming tutorials<p/>" 
                        "<P> We are currently undertaking Django which will help us implement other programs")

# Create your views here.
