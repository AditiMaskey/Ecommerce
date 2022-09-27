from django.contrib import admin
from . models import *
from django.utils.html import format_html


# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}
    
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'is_available', 'created_date', 'modified_date']
    list_filter = ['is_available', 'created_date', 'modified_date']
    list_editable = ['price', 'stock', 'is_available']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    list_display = ['product', 'get_image']
    
    def get_image(self, obj):
        if obj.images:
            return format_html('<img src="{}" width="50" />'.format(obj.images.url))
        return "No Image"

    get_image.short_description = 'Image'