from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from catalogue.models import *
from sitemenu.models import MenuItems

class CategoryList(ListView):
    template_name = 'catalogue/category_list.html'
    model = ProductCategory

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        context['categories'] = self.object_list
        context['page'] = MenuItems.objects.filter(is_catalogue_link = True).first()
        return context


class CategoryProductsList(ListView):
    template_name = 'catalogue/products_list.html'

    def get(self, request, *args, **kwargs):

        try:
            context = {}
            context['products'] = self.get_queryset()
            context['category'] = ProductCategory.objects.get(url=self.kwargs['category_url'])
            return render(request, self.template_name, context)
        except ObjectDoesNotExist:
            return render(request, '404.html', status=404)

    def get_queryset(self):
        return Product.objects.filter(category__url=self.kwargs['category_url'])



class ProductDetail(DetailView):
    template_name = 'catalogue/product_detail.html'
    model = Product
    slug_url_kwarg = 'product_url'
    slug_field = 'url'
    query_pk_and_slug = True

    def get(self, request, *args, **kwargs):

        try:
            context = {}
            product = Product.objects.get(url=self.kwargs['product_url'])
            context['product'] = product
            context['images'] = ProductImage.objects.filter(product=product)
            return render(request, self.template_name, context)

        except ObjectDoesNotExist:
            return render(request, '404.html', status=404)





















