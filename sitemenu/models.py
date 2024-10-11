from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):

    class Meta:
        verbose_name = u'Меню'
        verbose_name_plural = u'Меню'
        unique_together = ('title', 'menu_id')

    title = models.CharField(verbose_name=u'Название', max_length=20)
    menu_id = models.CharField(verbose_name=u'Идентификатор меню', max_length=20)


    def __str__(self):
        return self.title



class MenuItems(MPTTModel):

    class Meta:
        verbose_name = u'Пункты меню'
        verbose_name_plural = u'Пункты меню'


    title = models.CharField(verbose_name=u'Заголовок', max_length=20)
    url = models.SlugField(verbose_name='Url', null=True, blank=True, unique=True)
    parent = TreeForeignKey('self', verbose_name=u'Родитель', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu = models.ForeignKey(Menu, verbose_name=u'Меню', on_delete=models.CASCADE, null=True)
    page_template_name = models.CharField(verbose_name=u'Название шаблона страницы', max_length=20, null=True, blank=True)
    is_index_page = models.BooleanField(verbose_name=u'Главная страница', default=False)
    is_show = models.BooleanField(verbose_name=u'Показывать на сайте', default=True)
    is_catalogue_link = models.BooleanField(verbose_name=u'Ссылка на каталог', default=False)
    is_delivery_link = models.BooleanField(verbose_name=u'Ссылка на доставку', default=False)
    meta_title = models.CharField(verbose_name=u'Мета заголовок', max_length=255, null=True, blank=True)
    meta_description = models.CharField(verbose_name=u'Мета описание', max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(verbose_name=u'Мета ключевые слова', max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title

