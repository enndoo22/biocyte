from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


# Create your views here.

class MainPage(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'biocyte/main.html'
    extra_context = {'title': 'BIOCYTE'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем посты в контекст главной страницы
        context['posts'] = Post.objects.all().order_by('-date')
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'components/post_detail.html'  # Путь как в твоей структуре
    context_object_name = 'post'


class ProductListView(ListView):
    model = Product
    template_name = 'components/products.html' # Убедись, что файл лежит по этому пути
    context_object_name = 'products'

    def get_queryset(self):
        # Получаем слаг из URL и фильтруем товары
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаем саму категорию, чтобы написать её название в заголовке <h1>
        context['current_category'] = self.category
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'components/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем все картинки этого товара (у тебя это модель ImagesProduct)
        context['product_images'] = self.object.images.all()
        return context
