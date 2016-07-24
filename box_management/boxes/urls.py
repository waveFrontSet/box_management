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
        regex=r'^(?P<box>[\w-]+)/$',
        view=views.BoxItemListView.as_view(),
        name='items_by_box',
    ),

    url(
        regex=r'^(?P<box>[\w-]+)/take/$',
        view=views.BoxItemTakeListView.as_view(),
        name='item_take_list',
    ),

    url(
        regex=r'^(?P<box>[\w-]+)/return/$',
        view=views.BoxItemReturnListView.as_view(),
        name='item_return_list',
    ),

    url(
        regex=r'^(?P<box>[\w-]+)/take/(?P<pk>[\d]+)$',
        view=views.BoxItemTakeView.as_view(),
        name='item_take',
    ),

    url(
        regex=r'^(?P<box>[\w-]+)/return/(?P<pk>[\d]+)$',
        view=views.BoxItemReturnView.as_view(),
        name='item_return',
    ),

    url(
        regex=r'^(?P<box>[\w-]+)/(?P<category>[\w-]+)/$',
        view=views.BoxCategoryItemListView.as_view(),
        name='items_by_category',
    ),
]

