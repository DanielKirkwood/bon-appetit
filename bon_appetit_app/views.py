from django.shortcuts import render
from django.http import HttpResponse

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
    # the following is code segment to be implemented later
    """ restaurant_list = Restaurant.objects.order_by('-rating')[:6]
        context_dict["restaurants"] = restaurant_list
    """
    context = {}
    # add 'active' to context dict so show current page as active
    context["top_restaurants_page"] = "active"
    return render(request, 'top-restaurants.html', context=context)

def viewAccount(request):
    pass

def editAccount(request):
    pass
