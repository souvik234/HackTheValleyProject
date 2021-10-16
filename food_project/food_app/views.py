from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'food_app/home.html')

# Create your views here.
