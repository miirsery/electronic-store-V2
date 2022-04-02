from django.contrib import admin
from django.utils.safestring import mark_safe

from store.models import Category, Product, Subcategory, Comment
from user.models import User


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_now', 'quantity', 'status', 'get_image', )
    list_display_links = ('name', 'get_image', )
    search_fields = ('name', )
    list_filter = ('status', 'discount', 'cat', )
    ordering = ('name', )
    readonly_fields = ('get_image', )
    list_editable = ('status', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="100"')

    get_image.short_description = 'Фото товара'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    list_filter = ('active',)
    ordering = ('-created_at',)


admin.site.site_title = 'Администрирование Магазина'
admin.site.site_header = 'Администрирование Магазина'

