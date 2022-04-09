# Generated by Django 4.0.3 on 2022-04-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование категории')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Краткое описание')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('rate', models.PositiveIntegerField(choices=[(1, '1 - Terribly'), (2, '2 - Bad'), (3, '3 - Normal'), (4, '4 - Okay'), (5, '5 - Amazing')], null=True)),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Под категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='слаг подкатегории')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Описание товара')),
                ('short_description', models.CharField(blank=True, max_length=500, verbose_name='Краткое описание')),
                ('specifications', models.JSONField(blank=True, null=True, verbose_name='Характеристики')),
                ('price_now', models.FloatField(verbose_name='Текущая цена товара')),
                ('price_old', models.FloatField(blank=True, null=True, verbose_name='Старая цена товара')),
                ('quantity', models.PositiveIntegerField(verbose_name='Колличество товара на складе')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/products/%Y/%m/%d', verbose_name='Фото товара')),
                ('status', models.CharField(choices=[('Have', 'Есть в наличие'), ('Havent', 'Временно отсутствует')], default='Have', max_length=15, verbose_name='Стаус товара')),
                ('discount', models.BooleanField(verbose_name='Cкидка на товар')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_ad', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('cat', models.ManyToManyField(blank=True, null=True, to='store.category', verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
