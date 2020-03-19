from django.shortcuts import render
from django.http import HttpResponse
from bon_appetit_app.models import Restaurant, FoodItem
from django.db.models import Avg
from django.core import serializers

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

    rating_list = Restaurant.objects.all().order_by('-rating')[:6]
    context['rating_list'] = rating_list

    # get the 5 cheapest restaurants based on average price
    cheapest_list = Restaurant.objects.annotate(avg_price=Avg('fooditem__price')).order_by('avg_price')[:6]
    context['cheapest_list'] = cheapest_list

    # add 'active' to context dict so show current page as active
    context["top_restaurants_page"] = "active"
    return render(request, 'top-restaurants.html', context=context)

def viewPage(request, restaurant_name_slug):
    context = {}
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        menu = FoodItem.objects.filter(restaurant=restaurant)

        json_data = serializers.serialize("json", FoodItem.objects.all())

        context['json'] = json_data
        context['menu'] = menu
        context['restaurant'] = restaurant

    except Restaurant.DoesNotExist:
        context['restaurant'] = None

    return render(request, 'view-page.html', context=context)

def viewAccount(request):
    pass

def editAccount(request):
    pass
