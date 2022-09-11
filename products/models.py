from django.db import models


class Item(models.Model):
    """Модель товара"""
    name = models.CharField(max_length=56,
                            verbose_name='Название товара',
                            help_text='Введите название товара')
    description = models.TextField(verbose_name='описание товара',
                                   help_text='Опишите товар',
                                   blank=True,
                                   null=True)
    price = models.IntegerField(verbose_name='Цена (в центах)',
                                help_text='Введите цену (в центах)',
                                default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_price_in_dollars(self):
        return self.price / 100

