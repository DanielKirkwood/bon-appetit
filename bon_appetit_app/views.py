from django.shortcuts import render
from django.http import HttpResponse
from bon_appetit_app.models import Restaurant

def home(request):
    context = {}
    # add 'active' to context dict so show current page as active
    context["home_page"] = "active"
    return render(request, 'home.html', context=context)

def search(request):
    context = {}
    # add 'active' to context dict so show current page as active
    context["search_page"] = "active"
    return render(request, 'search.html', context=context)

def searchResults(request):
    pass

def topRestaurants(request):
    context = {}

    # add 'active' to context dict so show current page as active
    context["top_restaurants_page"] = "active"
    return render(request, 'top-restaurants.html', context=context)

def viewPage(request, restaurant_name_slug):
    context = {}
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        context['restaurant'] = restaurant

    except Restaurant.DoesNotExist:
        context['restaurant'] = None

    return render(request, 'view-page.html', context=context)

def viewAccount(request):
    pass

def editAccount(request):
    pass
