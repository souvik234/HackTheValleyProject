from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Recipe, ItemPurchased
from django.urls import reverse


def home(request):
    return render(request, 'food_app/home.html')

# Create your views here.
def InventoryView(request):
    context = {
        'items': ItemPurchased.objects.all()
    }
    return render(request, 'food_app/inventory.html', context=context)

def RecipeAvailableView(request):
    recipes = {
        "Wrap": {"Apples", "Chicken", "Carrots", "Turkey", "Lettuce", "Lentils"},
        "Salad": {"Lettuce", "Tomato", "Spinach", "Onions", "Walnut", "Lentils"},
        "Cake": {"Flour", "Milk", "Eggs", "Butter", "Carrots"},
        "Casserole": {"Cheese", "Nutmeg", "Chicken", "Butter", "Milk", "Onions"},
    }

    with open("ingredients.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        items_available = lines

    available_recipes = []
    for recipe, ingredients in recipes.items():
        if all(ingredient in items_available for ingredient in ingredients):
            available_recipes.append(recipe)

    item_context = {
        'items': available_recipes
    }

    return render(request, 'food_app/recipes_available.html', context=item_context)


def RecipeView(request):
    context = {
        'items': ItemPurchased.objects.all()
    }

    if request.method == "POST":
        items_available = request.POST.getlist("items")
        recipes = {
            "wrap": {"Apples", "Chicken", "Carrots", "Turkey", "Lettuce", "Lentils"},
            "salad": {"lettuce", "tomato", "spinach", "onion", "walnut", "lentil"},
            "cake": {"flour", "milk", "egg", "butter", "carrot"},
            "casserole": {"cheese", "nutmeg", "chicken", "butter", "milk", "onion"},
        }

        available_recipes = []
        for recipe, ingredients in recipes.items():
            if all(ingredient in items_available for ingredient in ingredients):
                available_recipes.append(recipe)

        item_context = {
            'items': available_recipes
        }

        with open('ingredients.txt', 'w') as f:
            for item in items_available:
                f.write("%s\n" % item)

        return redirect(reverse('food_app:Available-Recipes'))

    return render(request, 'food_app/recipes.html', context=context)