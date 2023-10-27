from django.contrib import admin

from webapp.models import Category, Product, ProductImage, Purchase

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(ProductImage)


# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'product', 'size', 'phone_number', 'delivery_address', 'created_at')
#     list_filter = ('created_at',)
#     search_fields = ('user__username', 'product__name', 'phone_number', 'delivery_address')
#     date_hierarchy = 'created_at'
#
#
# admin.site.register(Purchase, PurchaseAdmin)
