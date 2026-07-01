from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.
# admin.site.register(Category)

# admin.site.register(Product)
admin.site.register(ImagesProduct)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category_image')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}

    def category_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(
                f'<img src="{obj.image.url}" width="30" style="object-fit:cover;" />'
            )
        return '—'

    category_image.short_description = 'Image'


class ImageProductInline(admin.TabularInline):
    model = ImagesProduct
    fk_name = 'product'
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount', 'quantity', 'category', 'created_at', 'first_photo')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageProductInline]
    list_editable = ('price', 'discount', 'quantity')
    list_filter = ('discount', 'category', 'price')

    def first_photo(self, obj):
        if obj.images.exists():
            try:
                return mark_safe(f'<img src="{obj.images.first().image.url}" width="50">')
            except:
                return 'no image'
        else:
            return 'no image'

    first_photo.short_description = 'Фото продукта'


from django.contrib import admin
from .models import Post


from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    search_fields = ('title', 'category')
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = ('django_quill/django_quill.js',)
        css = {
            'all': (
                'django_quill/django_quill.css',
                'biocyte/css/quill_fix.css',
            )
        }

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
