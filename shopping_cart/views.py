import json
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, TemplateView
from .cart import Cart
from catalogue.models import Product
from order.forms import OrderForm


class ProductAdd(View):

    def get(self, request, *args, **kwargs):

        try:
            cart = Cart(self.request)
            product = Product.objects.get(id=self.kwargs['product_id'], in_stock=True)
            cart.add(product=product, quantity=int(request.GET['quantity']))
            context = {}
            context['items_count'] = len(cart)
            return HttpResponse(json.dumps(context), content_type="application/json", status=200)
        except ObjectDoesNotExist:
            return HttpResponse(json.dumps({'message':'Cart add error'}), content_type="application/json", status=500)





class ShoppingCartUpdate(View):


    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = Product.objects.get(id=self.kwargs['product_id'], in_stock=True)
        quantity = int(request.POST['quantity'])

        if quantity:
            cart.add(product=product, quantity=quantity, update_quantity=True)
            messages.info(request, u'Корзина успешно обновлена')
            return redirect(request.META['HTTP_REFERER'])


class RemoveProduct(View):

    def get(self, request, *args, **kwargs):
            cart = Cart(request)
            product = Product.objects.get(id=self.kwargs['product_id'])
            cart.remove(product)
            messages.info(request, u'Товар успешно удален из корзины')
            return redirect(request.META['HTTP_REFERER'])


class CartDetails(TemplateView):
    template_name = 'shopping_cart/cart.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['form'] = OrderForm()
        context['hide_cart_link'] = True
        return context













