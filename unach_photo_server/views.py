# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	DjangoProject,
	ProductionConfDjangoProject,
)


class DjangoProjectCreateView(CreateView):

    model = DjangoProject


class DjangoProjectDeleteView(DeleteView):

    model = DjangoProject


class DjangoProjectDetailView(DetailView):

    model = DjangoProject


class DjangoProjectUpdateView(UpdateView):

    model = DjangoProject


class DjangoProjectListView(ListView):

    model = DjangoProject


class ProductionConfDjangoProjectCreateView(CreateView):

    model = ProductionConfDjangoProject


class ProductionConfDjangoProjectDeleteView(DeleteView):

    model = ProductionConfDjangoProject


class ProductionConfDjangoProjectDetailView(DetailView):

    model = ProductionConfDjangoProject


class ProductionConfDjangoProjectUpdateView(UpdateView):

    model = ProductionConfDjangoProject


class ProductionConfDjangoProjectListView(ListView):

    model = ProductionConfDjangoProject

