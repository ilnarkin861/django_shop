from django.db import models
from catalogue.models import Product
from regional_centers.models import City

class Order(models.Model):

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'
        ordering = ('-id',)


    STATES = (
            ('INPROCESS', u'В обработке'),
            ('DONE', u'Выполнено'),
            ('ABORT', u'Отменено'),
    )

    name = models.CharField(verbose_name=u'ФИО', max_length=150)
    email = models.CharField(verbose_name=u'Электронный адрес', max_length=100)
    phone = models.CharField(verbose_name=u'Телефон', max_length=20)
    city = models.ForeignKey(City, verbose_name=u'Город', on_delete=models.CASCADE)
    address = models.CharField(verbose_name=u'Адрес', max_length=100)
    status = models.CharField(verbose_name=u'Статус', max_length=15, choices=STATES, default='INPROCESS')
    total_price = models.FloatField(verbose_name=u'Итоговая сумма', default=0)
    note = models.TextField(verbose_name=u'Заметки к заказу', null=True, blank=True)
    created_date = models.DateTimeField(verbose_name=u'Дата добавления', auto_now=True)


    def __str__(self):
        return u'Заказ № ' +str(self.id)



class OrderProduct(models.Model):

    class Meta:
        verbose_name = u'Заказанные продукты'
        verbose_name_plural = u'Заказанные продукты'


    order = models.ForeignKey(Order, verbose_name=u'Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=u'Продукт', on_delete=models.CASCADE)
    product_price = models.FloatField(verbose_name=u'Цена товара')
    quantity = models.IntegerField(verbose_name=u'Количество товара')

    def __str__(self):
        return self.product.title

    def get_total_price(self):
        return self.product_price * self.quantity