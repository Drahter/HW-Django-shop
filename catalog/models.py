from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение', upload_to='uploads/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(verbose_name='дата создания', null=True, auto_created=True)
    updated_at = models.DateTimeField(verbose_name='дата изменения', null=True, auto_now_add=True)

    def __str__(self):
        return f'{self.name}, категория {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
