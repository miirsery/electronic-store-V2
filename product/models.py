from django.db import models

# Create your models here.


class Product(models.Model):

    STATUS_PRODUCT = [
        ('Have', 'Товар в наличии'),
        ('Havent', 'Товар временно отсутвует')
    ]

    title = models.CharField(verbose_name='Товар', max_length=150, unique=True)
    description = models.TextField(verbose_name='О товаре', max_length=850)
    price_at_moment = models.PositiveIntegerField(
        verbose_name='Цена в данный момент'
    )
    quantity = models.IntegerField(
        verbose_name='Количество товара'
    )
    discounted_price = models.PositiveIntegerField(verbose_name='Скидка')
    year = models.IntegerField(
        verbose_name='Год выпуска', null=True, blank=True
    )
    color = models.CharField(
        verbose_name='Цвет товара', max_length=120
    )
    status = models.CharField(
        verbose_name='Статус товара', max_length=35,
        choices=STATUS_PRODUCT, default='Have'
    )
    # reviews = models.ForeignKey(
    #     'Review', verbose_name='Отзывы', on_delete=models.CASCADE,
    #     blank=True, null=True,
    # )
    created_ad = models.DateTimeField(
        verbose_name='Дата создания товара',
        auto_now_add=True
    )
    update_ad = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    photo = models.ImageField(
        verbose_name='Фото', upload_to='photos/%Y/%m/%d/',
        blank=True, null=True
    )
    cat = models.ForeignKey(
        'Category', verbose_name='Категория', blank=True, null=True,
        on_delete=models.PROTECT
    )
    slug = models.SlugField(
        verbose_name='Слаг', unique=True, db_index=True,
        max_length=255
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория', max_length=155, unique=True
    )
    description = models.TextField(
        verbose_name='Описание категории', max_length=255
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
