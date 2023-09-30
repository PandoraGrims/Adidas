from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ProductImage(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='images', on_delete=models.CASCADE,
                                verbose_name='Продукт')
    image = models.ImageField(upload_to="imgs", verbose_name='Изображение')

    def __str__(self):
        return f"Изображение для {self.product.name}"


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    code = models.CharField(max_length=100, null=False, blank=False, verbose_name="Артикул")
    price = models.CharField(max_length=100, null=False, blank=False, verbose_name='Цена')
    image = models.ManyToManyField(ProductImage, related_name='products', verbose_name='Изображения', blank=True)
    description = models.TextField(max_length=2000, verbose_name="Описание", null=True, blank=True,
                                   default=None)
    category = models.ForeignKey('webapp.Category', related_name='products_category', on_delete=models.CASCADE,
                                 verbose_name='Категория', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.pk} {self.name} {self.code}"

    def get_absolute_url(self):
        return reverse("webapp:index", kwargs={"pk": self.pk})

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductCategory(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='product_categories', on_delete=models.CASCADE,
                                verbose_name='Продукт')
    category = models.ForeignKey('webapp.Category', related_name='category_products', on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def __str__(self):
        return "{} | {}".format(self.product, self.category)
