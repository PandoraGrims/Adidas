from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.http import request, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from webapp.forms import ProductForm, ProductImageForm
from webapp.models import Product, Category, ProductImage

from django.contrib.auth import authenticate, login


def is_superuser(user):
    return user.is_superuser


class AdidasListView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    paginate_by = 9
    ordering = ("-created_at",)

    def get_queryset(self):
        products = super().get_queryset()
        return products


class CostumesListView(ListView):
    model = Product
    template_name = "products/costumes.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Costumes/Костюмы')
        return Product.objects.filter(category=category)


class CapsAndHastsListView(ListView):
    model = Product
    template_name = "products/caps_and_hats.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Caps&Hats/Кепки&Шапки')
        return Product.objects.filter(category=category)


class HoodiesListView(ListView):
    model = Product
    template_name = "products/hoodies.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Hoodies/Толстовки')
        return Product.objects.filter(category=category)


class JacketsListView(ListView):
    model = Product
    template_name = "products/jackets.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Jackets/Куртки')
        return Product.objects.filter(category=category)


class ShoesListView(ListView):
    model = Product
    template_name = "products/shoes.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Shoes/Обувь')
        return Product.objects.filter(category=category)


class TShirtsListView(ListView):
    model = Product
    template_name = "products/t-shirts.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='T-shirts/Футболки')
        return Product.objects.filter(category=category)


class TrousersListView(ListView):
    model = Product
    template_name = "products/trousers.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Trousers/Брюки')
        return Product.objects.filter(category=category)


class VestsListView(ListView):
    model = Product
    template_name = "products/vests.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Vests/Жилетки')
        return Product.objects.filter(category=category)


class ProductDetailView(DetailView):
    model = Product
    template_name = "crud/product_detail.html"
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получите объект продукта, с которым связано представление
        product = self.get_object()

        # Получите категорию продукта, если она связана с продуктом
        product_category = product.category

        # Получите изображения продукта, если они связаны с продуктом
        product_images = product.images.all()

        # Добавьте данные в контекст представления
        context['product_category'] = product_category
        context['product_images'] = product_images

        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'crud/product_create.html'
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        product = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)
        sizes = self.request.POST.getlist('sizes')
        product.sizes.set(sizes)
        return redirect('webapp:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'crud/product_update.html'
    success_url = reverse_lazy('webapp:index')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'crud/product_delete.html'
    success_url = reverse_lazy('webapp:index')


class ShippingPaymentView(TemplateView):
    template_name = "shipping_payment.html"


class ExchangeReturnView(TemplateView):
    template_name = "exchange_return.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"


class CategoryListView(TemplateView):
    template_name = "category_list.html"
