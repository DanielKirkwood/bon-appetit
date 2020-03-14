from random import randint
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bon_appetit_project.settings')

import django
django.setup()
from bon_appetit_app.models import City, Restaurant

def randomInt():
    return randint(0, 5)

def populate():
    Glasgow_restaurants = [{'name': 'Bread Meats Bread','address' : '79 Otago Street, G12', 'menu' : 'Burger', 'price' : 5}, 
                            {'name':'Oran Mor','address' : '79 Ashton Lane, G12', 'menu' : 'Haggis', 'price' : 10},
                            {'name':'Nandos','address' : '79 Gibson Street, G12', 'menu' : 'Chicken', 'price' : 7}]
    
    Edinburgh_restaurants = [{'name':'Greggs', 'address' : '79 Royal Mile, H12', 'menu' : 'Sausage Roll', 'price' : 1},
                            {'name':'Mcdees', 'address' : '79 Edinburgh Street, H12', 'menu' : 'McFlury', 'price' : 2},
                            {'name':'Starbucks', 'address' : '79 Somewhere Bld, H12', 'menu' : 'Coffee', 'price' : 3} ]
    
    Manchester_restaurants = [{'name':'Tony Macaroni', 'address' : '79 Manchester Street, M12', 'menu' : 'Macaroni', 'price' : 6},
                            {'name':'Le Petit Eloi', 'address' : '79 Roequefort Street, M12', 'menu' : 'Sandwich', 'price' : 5} ]

    cats = {'Glasgow': {'restaurants': Glasgow_restaurants},'Edinburgh': {'restaurants': Edinburgh_restaurants},'Manchester': {'restaurants': Manchester_restaurants} }
            
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['restaurants']:
            add_restaurant(c, p['name'], p['address'], p['menu'], randomInt(), p['price'])
    
    for c in City.objects.all():
        for p in Restaurant.objects.filter(city=c):
            print(f'- {c}: {p}')
            
def add_restaurant(cat, name, address, menu, rating, price=0,):
    p = Restaurant.objects.get_or_create(city=cat, name=name)[0]
    p.address = address
    p.menu = menu
    p.rating = rating
    p.price = price
    p.save()
    return p
    
def add_cat(name):
    c = City.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting bon_appetit population script..')
    populate()
            
            
            
            