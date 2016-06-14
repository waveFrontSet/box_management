from django.db import models

from box_management.users.models import User

from model_utils.models import TimeStampedModel
from model_utils import Choices


class Item(TimeStampedModel):
    STATUS = Choices('contained', 'taken by user')
    name = models.CharField()
    description = models.TextField(blank=True, null=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default=STATUS.contained, max_length=20)
    in_possession_of = models.ForeignKey(User, blank=True, null=True)


class ItemCategory(TimeStampedModel):
    name = models.CharField()


class Box(TimeStampedModel):
    name = models.CharField()
    location = models.CharField()
