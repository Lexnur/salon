# Generated by Django 5.0.1 on 2024-02-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_categoryproduct_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
    ]