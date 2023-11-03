from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.http import request, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpRequest
from webapp.forms import ProductForm, ProductImageForm, SearchForm, PurchaseForm
from webapp.models import Product, Category, ProductImage, Purchase, Size

from django.contrib.auth import authenticate, login


class PaginatedListView(ListView):
    items_per_page = 12
    page_url_param = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_number = self.request.GET.get(self.page_url_param)
        paginator = Paginator(self.get_queryset(), self.items_per_page)
        page = paginator.get_page(page_number)

        context['page'] = page

        return context


def is_superuser(user):
    return user.is_superuser


class AdidasListView(PaginatedListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    ordering = ("-created_at",)
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_value = self.request.GET.get('search')
        if search_value:
            queryset = queryset.filter(Q(name__icontains=search_value) | Q(description__icontains=search_value))
        return queryset


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


class PurchaseView(TemplateView):
    template_name = 'purchase/purchase_options.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = kwargs['product_id']
        product = get_object_or_404(Product, pk=product_id)
        context['product'] = product
        return context


# class ProductPurchaseView(CreateView):
#     model = Purchase
#     form_class = PurchaseForm
#     template_name = 'purchase/purchase_form_one.html'
#     success_url = reverse_lazy('webapp:purchase_success')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product = get_object_or_404(Product, pk=self.kwargs['product_id'])
#         context['product'] = product
#         context['sizes'] = product.sizes.all()
#         return context
#
#     def form_valid(self, form):
#         product = get_object_or_404(Product, pk=self.kwargs['product_id'])
#         form.instance.user = self.request.user
#         form.instance.product = product
#         return super().form_valid(form)

class PurchaseSuccessView(TemplateView):
    template_name = 'purchase/purchase_success.html'


class PurchaseNoDeliveryView(View):
    template_name = 'purchase/purchase_form_one.html'
    success_url = reverse_lazy('webapp:purchase_success')

    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        form = PurchaseForm(product=product)
        return render(request, self.template_name, {'product': product, 'form': form})

    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        phone = request.POST.get('phone_number')
        delivery_address = request.POST.get('delivery_address')
        size_id = request.POST.get('size')
        size = get_object_or_404(Size, pk=size_id)

        form = PurchaseForm(request.POST, product=product)

        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.product = product
            purchase.size = size
            purchase.phone_number = phone
            purchase.delivery_address = delivery_address
            purchase.save()
            return redirect(self.success_url)
        else:
            print(form.errors)
        return render(request, self.template_name, {'product': product, 'form': form})


class PurchaseWithDeliveryView(View):
    template_name = 'purchase/purchase_form_two.html'
    success_url = reverse_lazy('webapp:purchase_success')

    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        form = PurchaseForm(product=product)
        return render(request, self.template_name, {'product': product, 'form': form})

    def post(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        size_id = request.POST.get('size')
        size = get_object_or_404(Size, pk=size_id)

        form = PurchaseForm(request.POST, product=product)

        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.product = product
            purchase.size = size
            purchase.phone_number = phone
            purchase.address = address
            purchase.save()
            return redirect(self.success_url)
        else:
            print(form.errors)
        return render(request, self.template_name, {'product': product, 'form': form})


class PanelAdminView(TemplateView):
    template_name = 'panel.html'
