from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.http import request, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ProductImageForm
from webapp.models import Product, Category, ProductImage

from django.contrib.auth import authenticate, login


class AdidasListView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    paginate_by = 12
    ordering = ("-created_at",)

    def get_queryset(self):
        products = super().get_queryset()
        return products


class CostumesListView(ListView):
    model = Product
    template_name = "products/costumes.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Costumes/Костюмы')
        return Product.objects.filter(category=category)


class CapsAndHastsListView(ListView):
    model = Product
    template_name = "products/caps_and_hats.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Caps&Hats/Кепки&Шапки')
        return Product.objects.filter(category=category)


class HoodiesListView(ListView):
    model = Product
    template_name = "products/hoodies.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Hoodies/Толстовки')
        return Product.objects.filter(category=category)


class JacketsListView(ListView):
    model = Product
    template_name = "products/jackets.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Jackets/Куртки')
        return Product.objects.filter(category=category)


class ShoesListView(ListView):
    model = Product
    template_name = "products/shoes.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Shoes/Обувь')
        return Product.objects.filter(category=category)


class TShirtsListView(ListView):
    model = Product
    template_name = "products/t-shirts.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='T-shirts/Футболки')
        return Product.objects.filter(category=category)


class TrousersListView(ListView):
    model = Product
    template_name = "products/trousers.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Trousers/Брюки')
        return Product.objects.filter(category=category)


class VestsListView(ListView):
    model = Product
    template_name = "products/vests.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        category = get_object_or_404(Category, category_name='Vests/Жилетки')
        return Product.objects.filter(category=category)


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail_view.html"
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


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        # Создание продукта
        product = form.save()

        # Обработка изображений
        images = self.request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)

        return redirect('webapp:index')


# @method_decorator(login_required, name='dispatch')
# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'product_form.html'
#     success_url = reverse_lazy('webapp:index')
#
#     def form_valid(self, form):
#         # Создание продукта
#         product = form.save()
#
#         # Обработка изображений
#         new_images = self.request.FILES.getlist('image')  # Обращение к полю формы, не new_images
#         for image in new_images:
#             ProductImage.objects.create(product=product, image=image)
#
#         return redirect('webapp:index')

# for image in self.request.FILES.getlist('images'):
#     ProductImage.objects.create(product=product, image=image)
# return super().form_valid(form)

# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'your_template.html'
#     form_class = ProductForm
#
#     def form_valid(self, form):
#         # Сохранение товара
#         product = form.save()
#
#         # Обработка загрузки новых изображений
#         new_images = self.request.FILES.getlist('new_images')
#         for image in new_images:
#             ProductImage.objects.create(product=product, image=image)
#
#         return redirect('your_redirect_url')


# def create_product_image(request):
#     if request.method == 'POST':
#         form = ProductImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')  # Замените 'product_list' на URL вашего списка товаров
#     else:
#         form = ProductImageForm()
#     return render(request, 'create_product_image.html', {'form': form})


