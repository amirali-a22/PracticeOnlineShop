from django.contrib import admin

from shop.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
    list_display = ('name', 'price', 'available')
    list_editable = ('price', 'available')
    list_filter = ('available',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('sub_category',)
    list_display = ('name', 'is_sub')
    list_editable = ('is_sub',)
    list_filter = ('is_sub',)
    prepopulated_fields = {"slug": ("name",)}
