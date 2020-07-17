from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello World")

def home(request):
    return HttpResponse("<h1>Welcome to homepage<h1>")
    
def html_demo(request):
    return render(request,"sample7.html")