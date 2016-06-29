from test_plus.test import TestCase
from .models import Box, Item, ItemCategory


class BoxTests(TestCase):

    def setUp(self):
        Box.objects.get_or_create(name='Boxinator', location='Basement')

    def test_string_representation(self):
        box1 = Box.objects.get(name='Boxinator')
        self.assertEqual("'Boxinator', located in 'Basement'", str(box1))


class ItemTests(TestCase):

    def setUp(self):
        Box.objects.get_or_create(name='Boxinator', location='Basement')
        Box.objects.get_or_create(name='Ninchens Rumpelkiste', location='Living Room')
        ItemCategory.objects.get_or_create(name='Stuff')
        box1 = Box.objects.get(name='Boxinator')
        box2 = Box.objects.get(name='Ninchens Rumpelkiste')
        cat = ItemCategory.objects.get(name='Stuff')
        self.cable = Item.objects.create(name='Ethernet cable', box=box1, category=cat)
        self.manga = Item.objects.create(name='NGE Band 4', box=box2, category=cat)
        self.user = self.make_user()

    def test_string_representation(self):
        self.assertEqual('Ethernet cable, currently contained', str(self.cable))
        self.assertEqual('NGE Band 4, currently contained', str(self.manga))

    def test_take_item(self):
        self.manga.take_item(self.user)
        self.assertEqual(self.user, self.manga.in_possession_of)
        self.assertEqual('NGE Band 4, currently taken by user \'testuser\'', str(self.manga)) # name of the test user

    def test_return_item(self):
        self.manga.take_item(self.user)
        self.assertEqual(self.user, self.manga.in_possession_of)
        self.manga.return_item()
        self.assertEqual(self.manga.in_possession_of, None)

