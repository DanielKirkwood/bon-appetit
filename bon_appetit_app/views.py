from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from bon_appetit_app.models import Restaurant, FoodItem, UserProfile
from bon_appetit_app.forms import UserForm, UserProfileForm


def home(request):
    context = getregistered(request)
    # add 'active' to context dict so show current page as active
    context["home_page"] = "active"
    return render(request, 'home.html', context=context)

def search(request):
    context = getregistered(request)
    # add 'active' to context dict so show current page as active
    context["search_page"] = "active"

    if request.method == 'GET':

        querySet = Restaurant.objects.all()
        foodSet = FoodItem.objects.all()

        inputNameQuery = request.GET.get('inputName')
        inputCityQuery = request.GET.get('inputCity')
        inputRestrictionsQuery = request.GET.get('inputRestrictions')
        inputRatingQuery = request.GET.get('inputRating')

        if inputNameQuery != '' and inputNameQuery is not None:
            querySet = querySet.filter(name__icontains=inputNameQuery)
        
        if inputCityQuery != '' and inputCityQuery is not None:
            if inputCityQuery != 'Any':
                querySet = querySet.filter(city__name=inputCityQuery)

        if inputRestrictionsQuery != '' and inputRestrictionsQuery is not None:
            if inputRestrictionsQuery != 'None':
                foodSet = foodSet.filter(restriction=inputRestrictionsQuery)
                names = []
                for item in foodSet:
                    names.append(item.restaurant.name)
                querySet = querySet.filter(name__in=names)
        
        if inputRatingQuery != '' and inputRatingQuery is not None:
            if inputRatingQuery != 'None':
                querySet = querySet.filter(rating=int(inputRatingQuery))

        context['querySet'] = querySet

    return render(request, 'search.html', context=context)

def searchResults(request):
    pass

def topRestaurants(request):
    context = getregistered(request)

    rating_list = Restaurant.objects.all().order_by('-rating')[:6]
    context['rating_list'] = rating_list

    # get the 5 cheapest restaurants based on average price
    cheapest_list = Restaurant.objects.annotate(avg_price=Avg('fooditem__price')).order_by('avg_price')[:6]
    context['cheapest_list'] = cheapest_list

    # add 'active' to context dict so show current page as active
    context["top_restaurants_page"] = "active"
    return render(request, 'top-restaurants.html', context=context)

def viewPage(request, restaurant_name_slug):
    context = getregistered(request)
    try:
        restaurant = Restaurant.objects.get(slug=restaurant_name_slug)
        menu = FoodItem.objects.filter(restaurant=restaurant)

        context['menu'] = menu
        context['restaurant'] = restaurant

    except Restaurant.DoesNotExist:
        context['restaurant'] = None

    return render(request, 'view-page.html', context=context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('bon-appetit:home'))
            else:
                return HttpResponse("Your Bon Appetit account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            context = getregistered(request)
            context['invalid'] =  True
            context["home_page"] = "active"
            return render(request, 'home.html', context)

    else:
        return render(request, 'login.html')
        
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('bon-appetit:home'))

@login_required
def viewAccount(request):
    context = {}
    profile = UserProfile.objects.get(user=request.user)
    context['profile'] = profile
    return render(request, 'view-account.html', context=context)
    
@login_required
def editAccount(request):
    context = {}
    profile = UserProfile.objects.get(user=request.user)
    context['profile'] = profile
    return render(request, 'edit-account.html', context=context)

def getregistered(request):

    context = {}
    registered = False
    
    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
        
            user.set_password(user.password)
            user.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user
        
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            print(profile)
            profile.save()
        
            registered =True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    context['user_form'] = user_form
    context['profile_form'] = profile_form
    context['registered'] = registered

    return context