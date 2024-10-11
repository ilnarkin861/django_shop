from django.template.loader import render_to_string
from django.utils.html import strip_tags

def order_from_managers(order):
    context = {}
    context['order_id'] = order
    context['name'] = order.name
    context['email'] = order.email
    context['phone'] = order.phone
    context['city'] = order.city
    context['address'] = order.address
    context['total_price'] = order.total_price
    return render_to_string('email/order_for_managers.html', {'order':order})


def contacts(object):
    context = {}
    context['name'] = object['name']
    context['email'] = object['email']
    context['message'] = object['message']
    return render_to_string('email/contact.html', {'data':context})