# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import ListView, UpdateView, CreateView, DeleteView, RedirectView
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin, FormValidMessageMixin

from .models import Box, ItemCategory, Item


class BoxListView(ListView):
    model = Box


class BoxItemListView(ListView):
    template_name = "boxes/items_by_box.html"
    context_object_name = "item_list"

    def get_queryset(self):
        self.box = get_object_or_404(Box, name=self.kwargs['box'])
        return Item.objects.filter(box=self.box)

    def get_context_data(self, **kwargs):
        context = super(BoxItemListView, self).get_context_data(**kwargs)
        context['box'] = self.box
        return context


class BoxCategoryItemListView(BoxItemListView):
    template_name = "boxes/items_by_category.html"

    def get_queryset(self):
        self.category = get_object_or_404(ItemCategory, name=self.kwargs['category'])
        query_set = super(BoxCategoryItemListView, self).get_queryset()
        return query_set.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(BoxCategoryItemListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class BoxItemTakeListView(LoginRequiredMixin, BoxItemListView):
    template_name = "boxes/take_items.html"

    def get_queryset(self):
        query_set = super(BoxItemTakeListView, self).get_queryset()
        return query_set.filter(status="contained")


class BoxItemReturnListView(LoginRequiredMixin, BoxItemListView):
    template_name = "boxes/return_items.html"

    def get_queryset(self):
        query_set = super(BoxItemReturnListView, self).get_queryset()
        return query_set.filter(in_possession_of=self.request.user)


class BoxItemTakeView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs['pk'])
        item.give_to(self.request.user)
        return reverse('boxes:item_take_list', kwargs={'box': kwargs['box']})


class BoxItemReturnView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs['pk'])
        item.return_to_box()
        return reverse('boxes:item_return_list', kwargs={'box': kwargs['box']})
