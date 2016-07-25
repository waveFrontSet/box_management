# The sole purpose of this file is to quickly generate initial data.
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
from box_management.boxes.models import Box, ItemCategory, Item



BOX_KEYS = ['name', 'location']
CATEGORY_KEYS = ['name']
ITEM_KEYS = ['name', 'description', 'box', 'category']

BOX_VALUES = [
    ['Boxinator', 'Keller'],
    ['Rumpelkiste', 'Keller'],
    ['Zeugskarton', 'Keller'],
]

CATEGORY_VALUES = [
    ['Elektronisches'],
    ['Bücher'],
    ['Sonstiges'],
]


def add_box(name, location):
    b = Box.objects.get_or_create(name=name, location=location)[0]
    return b


def add_cat(name):
    c = ItemCategory.objects.get_or_create(name=name)[0]
    return c


def add_item(name, description, box, category):
    i = Item.objects.get_or_create(name=name, description=description, box=box, category=category)
    return i


def populate():
    for box_v in BOX_VALUES:
        add_box(**dict(zip(BOX_KEYS, box_v)))
    for cat_v in CATEGORY_VALUES:
        add_cat(**dict(zip(CATEGORY_KEYS, cat_v)))

    boxinator = Box.objects.get(name='Boxinator')
    rumpelkiste = Box.objects.get(name='Rumpelkiste')
    zeugskarton = Box.objects.get(name='Zeugskarton')
    elektronisches = ItemCategory.objects.get(name='Elektronisches')
    buecher = ItemCategory.objects.get(name='Bücher')
    sonstiges = ItemCategory.objects.get(name='Sonstiges')

    boxielek = [boxinator, elektronisches]
    rumpelbuch = [rumpelkiste, buecher]
    zeugssonst = [zeugskarton, sonstiges]

    item_values = [
        ['Kabel', 'Irgendein Kabel'] + boxielek,
        ['Ethernet Kabel', 'Das Rote(!)'] + boxielek,
        ['Wii controller', 'Ohne Wii Motion Plus'] + boxielek,
        ['Wii Ständer', 'Ist n bisschen eingerissen...'] + boxielek,
        ['NGE Band 1', 'Cooles Zeug dadrin...'] + rumpelbuch,
        ['NGE Band 2', 'Weisheits Lieblingsbuch'] + rumpelbuch,
        ['LTB Nr. 1', 'Neuauflage, aber trotzdem cool.'] + rumpelbuch,
        ['LTB Nr. 145', 'Pauls Favorit'] + rumpelbuch,
        ['Huberts Hut', 'Wie kommt der denn hierein?'] + zeugssonst,
        ['Norayas Bogensehne', 'In nem Raid gerissen'] + zeugssonst,
        ['Ravys Haschpfeife', 'Irgendwie muss man ja ausspannen...'] + zeugssonst,
    ]

    for item_v in item_values:
        add_item(**dict(zip(ITEM_KEYS, item_v)))

    for box in Box.objects.all():
        print("Box {box}:".format(box=box))
        print("-"*20)
        for item in Item.objects.filter(box=box):
            print("{item}".format(item=item))
        print("-"*20)

if __name__ == '__main__':
    print("Start population script...")
    populate()
