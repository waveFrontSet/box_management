# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin, FormValidMessageMixin

from .models import Box, ItemCategory, Item


class BoxListView(ListView):
    model = Box


class BoxItemListView(ListView):
    template_name = "boxes/items_by_box.html"
    context_object_name = "item_list"

    def get_queryset(self):
        self.box = get_object_or_404(Box, name=self.args[0])
        return Item.objects.filter(box=self.box)

    def get_context_data(self, **kwargs):
        context = super(BoxItemListView, self).get_context_data(**kwargs)
        context['box'] = self.box
        return context
