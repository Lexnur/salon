from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')

    class Meta:
        verbose_name = "Категорию товара"
        verbose_name_plural = "Категории товаров"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='shop_images/', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    # quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)  # Сортировка товаров по id

    def __str__(self):
        return self.name

    def discount_price(self):  # Расчет скидки товара
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={"goods_slug": self.slug})
