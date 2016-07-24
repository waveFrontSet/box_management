from django.db import models
from django.utils.translation import ugettext as _

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
    STATUS = Choices(('contained', _('contained')), ('taken', _('taken by user')))
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default=STATUS.contained, max_length=20)
    in_possession_of = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        status = self.get_status_display()
        ret_string = "{name}, currently {status}".format(name=self.name, status=status)
        if self.status == self.STATUS.taken:
            ret_string += " '{user}'".format(user=self.in_possession_of)
        return ret_string

    def give_to(self, user):
        self.status = self.STATUS.taken
        self.in_possession_of = user

    def return_to_box(self):
        self.status = self.STATUS.contained
        self.in_possession_of = None
