from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product


class AdidasListView(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"
    paginate_by = 12
    ordering = ("-created_at",)

    def get_queryset(self):
        products = super().get_queryset()
        if self.request.user.is_authenticated:
            products = products.filter(author=self.request.user)
        return products
