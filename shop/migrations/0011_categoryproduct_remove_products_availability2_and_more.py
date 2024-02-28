# Generated by Django 5.0.1 on 2024-02-27 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_delete_categoryproduct_products_availability2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Вид товара',
            },
        ),
        migrations.RemoveField(
            model_name='products',
            name='availability2',
        ),
        migrations.AddField(
            model_name='products',
            name='category_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.categoryproduct', verbose_name='Вид товара'),
        ),
    ]