# Generated by Django 3.2.15 on 2022-09-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название товара', max_length=56, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, help_text='Опишите товар', null=True, verbose_name='описание товара')),
                ('price', models.IntegerField(default=0, help_text='Введите цену', verbose_name='Цена')),
            ],
        ),
    ]
