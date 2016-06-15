from django.db import models

from box_management.users.models import User

from model_utils.models import TimeStampedModel
from model_utils import Choices


class Box(TimeStampedModel):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return "'{b.name}', located in '{b.location}'".format(b=self)


class ItemCategory(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(TimeStampedModel):
    STATUS = Choices('contained', ('taken', 'taken by user'))
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default=STATUS.contained, max_length=20)
    in_possession_of = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return "{i.name}, currently {i.status}".format(i=self)

    def take_item(self, user):
        self.status = self.STATUS.taken
        self.in_possession_of = user

    def return_item(self):
        self.status = self.STATUS.contained
        self.in_possession_of = None
