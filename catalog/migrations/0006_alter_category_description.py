# Generated by Django 5.1 on 2024-08-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_category_name_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=500, verbose_name='описание'),
        ),
    ]
