# Generated by Django 3.2.15 on 2022-09-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0, help_text='Введите цену (в центах)', verbose_name='Цена (в центах)'),
        ),
    ]
