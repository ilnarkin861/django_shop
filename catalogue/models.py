from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ivangreenway.utils import translit

class ProductCategory(MPTTModel):
    class Meta:
        verbose_name = u'Категория продукта'
        verbose_name_plural = u'Категории продукта'

    title = models.CharField(verbose_name=u'Название категории', max_length=30,)
    url = models.SlugField(verbose_name=u'Ссылка категории', max_length=30, null=True, blank=True, unique=True,
                           help_text=u'Если оставить пустым, ссылка будет сгенерирована из названия. Должна быть уникальной.')
    parent = TreeForeignKey('self', verbose_name=u'Родительская категория', on_delete=models.CASCADE, null=True,
                            blank=True,
                            related_name='product_category_children')
    short_description = models.TextField(verbose_name=u'Короткое описание категории', null=True, blank=True)
    description = models.TextField(verbose_name=u'Описание категории', null=True, blank=True)
    image = models.ImageField(verbose_name=u'Изображение категории', null=True, blank=True, upload_to='images/catalog/category')
    meta_title = models.CharField(verbose_name=u'Мета заголовок', max_length=255, null=True, blank=True)
    meta_description = models.CharField(verbose_name=u'Мета описание', max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(verbose_name=u'Мета ключевые слова', max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.url:
            self.url = translit(self.url.lower())

        else:
            self.url = translit(self.title.lower())


        super(ProductCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        url = "/%s/" % self.url
        page = self
        while page.parent:
            url = "/%s%s" % (page.parent.url, url)
            page = page.parent
        return url

    def get_descendants(self, include_self=True):
        return super().get_descendants(include_self)


class Product(models.Model):
    class Meta:
        verbose_name = u'Продукты Greenway'
        verbose_name_plural = u'Продукты Greenway'

    title = models.CharField(verbose_name=u'Название продукта', max_length=100, )
    url = models.SlugField(verbose_name=u'Ссылка продукта', max_length=100, null=True, blank=True, unique=True,
                           help_text=u'Если оставить пустым, ссылка будет сгенерирована из названия. Должна быть уникальной.')
    vendor_code = models.CharField(verbose_name=u'Артикул', max_length=10, null=True, blank=True)
    short_description = models.TextField(verbose_name=u'Короткое описание продукта', null=True, blank=True)
    description = models.TextField(verbose_name=u'Подробное описание продукта', null=True, blank=True)
    price = models.FloatField(verbose_name=u'Цена продукта')
    thumbnail = models.ImageField(verbose_name=u'Маленькое изображение продукта', null=True, blank=True, upload_to='images/catalog/products/thumb/%Y-%m-%d/')
    category = models.ManyToManyField(ProductCategory, verbose_name=u'Категория продукта', related_name='product_category')
    in_stock = models.BooleanField(verbose_name=u'В наличии', default=True)
    is_popular = models.BooleanField(verbose_name=u'Популярные продукты', default=False)
    meta_title = models.CharField(verbose_name=u'Мета заголовок', max_length=255, null=True, blank=True)
    meta_description = models.CharField(verbose_name=u'Мета описание', max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(verbose_name=u'Мета ключевые слова', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.url:
            self.url = translit(self.url.lower())

        else:
            self.url = translit(self.title.lower())

        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):

    class Meta:
        verbose_name = u'Изображение продукта'
        verbose_name_plural = u'Изображения продукта'


    product = models.ForeignKey(Product, verbose_name=u'Продукт', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=u'Изображение товара', null=True, blank=True, upload_to='images/catalog/products/big/%Y-%m-%d/')
    is_main_image = models.BooleanField(verbose_name=u'Главное изображение', default=False)