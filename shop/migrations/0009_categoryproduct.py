# Generated by Django 5.0.1 on 2024-02-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_products_series'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Вид товара',
            },
        ),
    ]
