from random import randint
from bon_appetit_project import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bon_appetit_project.settings')

import django
django.setup()
from bon_appetit_app.models import City, Restaurant, FoodItem, Menu

def populate():

    greggs_food = [
        {'name': 'Mexican Chicken Baugette', 'price': 1.30, 'restriction': 'None'},
        {'name': 'Ham & Cheese sandwich', 'price': 1.30, 'restriction': 'Vegetarian'},
        {'name': 'Sausage Roll', 'price': 0.80, 'restriction': 'None'},
        {'name': 'Yum Yum', 'price': 0.60, 'restriction': 'Vegan'},
    ]

    bread_meets_bread_food = [
        {'name': 'Black and Blue Burger', 'price': 9.50, 'restriction': 'None'},
        {'name': 'Classic Burger', 'price': 8.00, 'restriction': 'None'},
        {'name': 'Vegan Caribbean Burger', 'price': 9.50, 'restriction': 'None'},
        {'name': 'Vegan Cheesebruger', 'price': 9.00, 'restriction': 'Vegan'},
    ]

    oran_mor_food = [
        {'name': '6oz Rump Steak with Rosti Potatoes', 'price': 11.50, 'restriction': 'None'},
        {'name': 'Hake Fillet with Lemon Crushed Potatoes', 'price': 10.00, 'restriction': 'None'},
        {'name': 'Spiced Lentil and Sweet Potato Casserole', 'price': 11.20, 'restriction': 'Vegetarian'},
    ]

    nandos_food = [
        {'name': 'Chicken Butterfly', 'price': 11.75, 'restriction': 'None'},
        {'name': 'Portobello Mushroom & Halloumi Burger', 'price': 10.75, 'restriction': 'Vegetarian'},
        {'name': 'Mozam Wrap', 'price': 10.85, 'restriction': 'None'},
    ]

    mcdees_food = [
        {'name': 'Big Mac', 'price': 3.19, 'restriction': 'None'},
        {'name': 'Chicken Nuggets 6 piece', 'price': 3.19, 'restriction': 'None'},
        {'name': 'The Spicy Veggie One', 'price': 2.99, 'restriction': 'Vegetarian'},
    ]

    starbucks_food = [
        {'name': 'Vanilla Spiced Latte (Tall)', 'price': 3.25, 'restriction': 'Vegetarian'},
        {'name': 'Caffe Americano', 'price': 1.95, 'restriction': 'Vegetarian'},
        {'name': 'Cheese & Marmite Sandwich', 'price': 2.85, 'restriction': 'Vegetarian'},
    ]

    tony_macaroni_food = [
        {'name': 'Margherita Pizza', 'price': 5.95, 'restriction': 'Vegan'},
        {'name': 'Diavola Pizza', 'price': 5.95, 'restriction': 'None'},
        {'name': 'Penne Arrabbiata', 'price': 5.95, 'restriction': 'Vegetarian'},
    ]

    le_petit_eloi_food = [
        {'name': 'Le Poulet Entier', 'price': 23.00, 'restriction': 'None'},
        {'name': 'Les Gnocchis', 'price': 14.50, 'restriction': 'Vegan'},
        {'name': 'La Salade', 'price': 14.50, 'restriction': 'Vegetarian'},
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
            restaurant = add_restaurant(city, p['name'], p['address'], randomInt(), assignImage())
            menu = add_menu(restaurant, restaurant.name)
            for f in p['menu']:
                print(menu.restaurant_name)
                print(f)
                food = add_food(menu, f['name'], f['price'], f['restriction'])


    for c in City.objects.all():
        for p in Restaurant.objects.filter(city=c):
            print(f'- {c}: {p}')


def add_menu(restaurant, restaurant_name):
    menu = Menu.objects.get_or_create(restaurant=restaurant)[0]
    menu.restaurant_name = restaurant_name
    menu.save()
    return menu
    
def add_food(menu, name, price, restriction):
    f = FoodItem.objects.get_or_create(menu=menu, name=name)[0]
    f.menu = menu
    f.name = name
    f.price = price
    f.restriction = restriction
    f.save()
    return f
            
def add_restaurant(city, name, address, rating, image):
    restaurant = Restaurant.objects.get_or_create(city=city, name=name)[0]
    restaurant.address = address
    restaurant.rating = rating
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

if __name__ == '__main__':
    print('Starting bon_appetit population script..')
    populate()
            
            
            
            