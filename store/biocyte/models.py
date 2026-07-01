from django.db import models
from django_quill.fields import QuillField


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True, null=True, verbose_name='Слаг категории')
    image = models.ImageField(upload_to='categories/', verbose_name="Изображение")

    def __str__(self):
        return self.title

    def cat_image(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    slug = models.SlugField(unique=True, null=True, verbose_name='Слаг продукта')
    desc = models.TextField(verbose_name='Описание продукта')
    use_instructions = models.TextField(verbose_name="Способ применения")
    composition = models.TextField(verbose_name="Состав")
    price = models.IntegerField(verbose_name='Цена продукта', null=True, blank=True, default=0)
    discount = models.IntegerField(verbose_name='Скидка', null=True, blank=0, default=0)
    quantity = models.IntegerField(verbose_name='Кол-во продукта', default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='products')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ImagesProduct(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Фото продукта')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='images')

    def __str__(self):
        return f'Фото продукта {self.product.title}'

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'




class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    category = models.CharField(max_length=100, verbose_name="Категория")
    excerpt = models.TextField(verbose_name="Краткое описание")
    content = QuillField(verbose_name="Полный текст статьи")
    image = models.ImageField(upload_to='blog_images/', verbose_name="Изображение")
    date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class SiteSettings(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", default="+")
    address = models.TextField(verbose_name="Адрес", blank=True)
    instagram = models.URLField(verbose_name="Ссылка Instagram", blank=True)
    telegram = models.URLField(verbose_name="Ссылка Telegram", blank=True)
    facebook = models.URLField(verbose_name="Ссылка Facebook", blank=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Общие настройки сайта"