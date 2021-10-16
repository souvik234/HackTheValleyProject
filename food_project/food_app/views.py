from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Recipe, ItemPurchased

def home(request):
    return render(request, 'food_app/home.html')

# Create your views here.
def InventoryView(request):
    context = {
        'items': ItemPurchased.objects.all()
    }
    return render(request, 'food_app/inventory.html', context=context)