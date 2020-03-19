from random import randint
from bon_appetit_project import settings
import os
from django.db.models import Avg
from django.db.models import Func
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bon_appetit_project.settings')

import django
django.setup()
from bon_appetit_app.models import City, Restaurant, FoodItem

def populate():

    greggs_food = [
        {'name': 'Mexican Chicken Baugette', 'price': 1.30, 'restriction': 'None', 'rating': 3},
        {'name': 'Ham & Cheese sandwich', 'price': 1.30, 'restriction': 'Vegetarian', 'rating': 1},
        {'name': 'Sausage Roll', 'price': 0.80, 'restriction': 'None', 'rating': 4},
        {'name': 'Yum Yum', 'price': 0.60, 'restriction': 'Vegan', 'rating': 5},
    ]

    bread_meets_bread_food = [
        {'name': 'Black and Blue Burger', 'price': 9.50, 'restriction': 'None', 'rating': 4},
        {'name': 'Classic Burger', 'price': 8.00, 'restriction': 'None', 'rating': 3},
        {'name': 'Vegan Caribbean Burger', 'price': 9.50, 'restriction': 'None', 'rating': 5},
        {'name': 'Vegan Cheesebruger', 'price': 9.00, 'restriction': 'Vegan', 'rating': 4},
    ]

    oran_mor_food = [
        {'name': '6oz Rump Steak with Rosti Potatoes', 'price': 11.50, 'restriction': 'None', 'rating': 5},
        {'name': 'Hake Fillet with Lemon Crushed Potatoes', 'price': 10.00, 'restriction': 'None', 'rating': 1},
        {'name': 'Spiced Lentil and Sweet Potato Casserole', 'price': 11.20, 'restriction': 'Vegetarian', 'rating': 3},
    ]

    nandos_food = [
        {'name': 'Chicken Butterfly', 'price': 11.75, 'restriction': 'None', 'rating': 3},
        {'name': 'Portobello Mushroom & Halloumi Burger', 'price': 10.75, 'restriction': 'Vegetarian', 'rating': 5},
        {'name': 'Mozam Wrap', 'price': 10.85, 'restriction': 'None', 'rating': 5},
    ]

    mcdees_food = [
        {'name': 'Big Mac', 'price': 3.19, 'restriction': 'None', 'rating': 2},
        {'name': 'Chicken Nuggets 6 piece', 'price': 3.19, 'restriction': 'None', 'rating': 5},
        {'name': 'The Spicy Veggie One', 'price': 2.99, 'restriction': 'Vegetarian', 'rating': 1},
    ]

    starbucks_food = [
        {'name': 'Vanilla Spiced Latte (Tall)', 'price': 3.25, 'restriction': 'Vegetarian', 'rating': 1},
        {'name': 'Caffe Americano', 'price': 1.95, 'restriction': 'Vegetarian', 'rating': 2},
        {'name': 'Cheese & Marmite Sandwich', 'price': 2.85, 'restriction': 'Vegetarian', 'rating': 3},
    ]

    tony_macaroni_food = [
        {'name': 'Margherita Pizza', 'price': 5.95, 'restriction': 'Vegan', 'rating': 3},
        {'name': 'Diavola Pizza', 'price': 5.95, 'restriction': 'None', 'rating': 4},
        {'name': 'Penne Arrabbiata', 'price': 5.95, 'restriction': 'Vegetarian', 'rating': 5},
    ]

    le_petit_eloi_food = [
        {'name': 'Le Poulet Entier', 'price': 23.00, 'restriction': 'None', 'rating': 2},
        {'name': 'Les Gnocchis', 'price': 14.50, 'restriction': 'Vegan', 'rating': 1},
        {'name': 'La Salade', 'price': 14.50, 'restriction': 'Vegetarian', 'rating': 1},
    ]


    Glasgow_restaurants = [{'name': 'Bread Meats Bread','address' : '79 Otago Street, G12', 'menu': bread_meets_bread_food}, 
                            {'name':'Oran Mor','address' : '79 Ashton Lane, G12', 'menu': oran_mor_food},
                            {'name':'Nandos','address' : '79 Gibson Street, G12', 'menu': nandos_food}]
    
    Edinburgh_restaurants = [{'name':'Greggs', 'address' : '79 Royal Mile, H12', 'menu': greggs_food},
                            {'name':'Mcdees', 'address' : '79 Edinburgh Street, H12', 'menu': mcdees_food},
                            {'name':'Starbucks', 'address' : '79 Somewhere Bld, H12', 'menu': starbucks_food} ]
    
    Manchester_restaurants = [{'name':'Tony Macaroni', 'address' : '79 Manchester Street, M12', 'menu': tony_macaroni_food},
                            {'name':'Le Petit Eloi', 'address' : '79 Roequefort Street, M12', 'menu': le_petit_eloi_food}]

    cities = {'Glasgow': {'restaurants': Glasgow_restaurants},'Edinburgh': {'restaurants': Edinburgh_restaurants},'Manchester': {'restaurants': Manchester_restaurants} }

    menues = {'Greggs': {'menu': greggs_food}, 'Mcdees': {'menu': mcdees_food}, 
    'Tony Macaroni': {'menu': tony_macaroni_food}, 'Starbucks': {'menu': starbucks_food},
    'Le Petit Eloi': {'menu': le_petit_eloi_food}, 'Bread Meats Bread': {'menu': bread_meets_bread_food},
    'Oran Mor': {'menu': oran_mor_food}, 'Nandos': {'menu': nandos_food}}
    
    for city, city_data in cities.items():
        city = add_city(city)
        for p in city_data['restaurants']:
            restaurant = add_restaurant(city, p['name'], p['address'], assignImage())

            for f in p['menu']:
                food = add_food(restaurant, f['name'], f['price'], f['restriction'], f['rating'])

        # update the restaurants average rating based off menu items ratings
        for r in Restaurant.objects.all():
            total = 0
            count = 0
            for f in FoodItem.objects.filter(restaurant=r):
                total += f.rating
                count += 1
            average = total/count
            r.rating = average
            r.save()

    for c in City.objects.all():
        for p in Restaurant.objects.filter(city=c):
            print(f'- {c}: {p}')
    
def add_food(restaurant, name, price, restriction, rating):
    f = FoodItem.objects.get_or_create(restaurant=restaurant, name=name)[0]
    f.restaurant = restaurant
    f.name = name
    f.price = price
    f.restriction = restriction
    f.rating = rating
    f.save()
    return f
            
def add_restaurant(city, name, address, image):
    restaurant = Restaurant.objects.get_or_create(city=city, name=name)[0]
    restaurant.address = address
    restaurant.picture = image
    restaurant.save()
    return restaurant
    
def add_city(name):
    city = City.objects.get_or_create(name=name)[0]
    city.save()
    return city


def randomInt():
    return randint(0, 5)

def assignImage():
    root = settings.MEDIA_ROOT
    entries = os.listdir(root)
    size = len(entries)
    select = randint(0, size-1)
    return entries[select]

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 0)'


if __name__ == '__main__':
    print('Starting bon_appetit population script..')
    populate()
            
            
            
            