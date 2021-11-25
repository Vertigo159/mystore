from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование категории")
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta():
        db_table = "категории"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    category = models.ManyToManyField(Category)
    image = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    slug = models.SlugField(max_length=50, unique=True)


    def __str__(self):
        return self.title

    class Meta():
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
    


