from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:category_slug>/', ProductListView.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
