# Generated by Django 5.1 on 2024-08-29 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(null=True, verbose_name='дата создания'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='изображение'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='наименование'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(null=True, verbose_name='дата изменения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='наименование'),
        ),
    ]
