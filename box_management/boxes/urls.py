# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.BoxListView.as_view(),
        name='boxlist',
    ),

    url(
        regex=r'^/([\w-]+)/$',
        view=views.BoxItemListView.as_view(),
        name='items_by_box',
    ),
]

