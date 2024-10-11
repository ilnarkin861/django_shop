from django.shortcuts import redirect
from django.conf import settings
from smtplib import SMTPException
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib import messages
from .forms import *
from shopping_cart.cart import Cart
from .models import *
from ivangreenway.email_utils import order_from_managers

class PermissionDeniedMixin():

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class OrderCreation(CreateView):
    success_message = u'Ваш заказ успешно отправлен. Скоро мы с вами свяжемся для уточнения деталей заказа.'
    error_message = u'Ошибка при оформление заказа. Попробуйте еще раз.'
    form_class = OrderForm
    success_url = '/cart'

    def form_valid(self, form):

        try:
            cart = Cart(self.request)
            if len(cart) > 0:
                order = form.save(commit=False)
                order.total_price = cart.get_total_price()
                order.save()


                products = []
                for item in cart:
                    product = OrderProduct(
                                        order = order,
                                        product = item['product'],
                                        product_price = item['price'],
                                        quantity = item['quantity']
                                )

                    products.append(product)
                OrderProduct.objects.bulk_create(products)
                #email_content = order_from_managers(order)
                #message = EmailMultiAlternatives(u'Новый заказ', email_content, settings.EMAIL_HOST_USER, settings.EMAIL_LIST)
                #message.attach_alternative(email_content, "text/html")
                #message.send()
                #cart.clear()
                messages.info(self.request, self.success_message)
                return super().form_valid(form)
        except SMTPException:
            messages.error(self.request, self.error_message)
            return redirect(self.success_url)

        return None




class OrderList(PermissionDeniedMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'order_list'


class OrderDetails(PermissionDeniedMixin, DetailView):
    model = Order
    template_name = 'order/order_details.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['order'] = self.object
        order_form = OrderChangeForm()
        order_form.fields['status'].initial = self.object.status
        context['order_form'] = order_form
        context['products'] = OrderProduct.objects.filter(order=self.object)
        return context


class OrderUpdate(PermissionDeniedMixin, UpdateView):
    model = Order
    fields = ('status',)
    success_url = '/order/list/'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        messages.info(self.request, u'Заказ успешно обновлен')
        return super().form_valid(form)











