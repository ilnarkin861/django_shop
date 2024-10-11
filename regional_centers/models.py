from django.db import models

class City(models.Model):

    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'
        ordering = ('city_name',)

    city_name = models.CharField(verbose_name=u'Название города', max_length=100, unique=True)


    def __str__(self):
        return self.city_name



class CenterInfo(models.Model):

    class Meta:
        verbose_name = u'Информация о центре'
        verbose_name_plural = u'Информация о центре'
        ordering = ('center_name',)

    center_name = models.CharField(verbose_name=u'Название центра', max_length=100)
    city = models.ForeignKey(City, verbose_name=u'Город', on_delete=models.CASCADE)
    address = models.CharField(verbose_name=u'Адрес центра', max_length=255)
    openning_hours = models.CharField(verbose_name=u'Режим работы', max_length=255, null=True, blank=True)


    def __str__(self):
        return self.city.city_name +', ' +self.address

    def get_center_name(self):
        return self.__str__()


