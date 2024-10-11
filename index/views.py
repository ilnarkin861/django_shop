from django.views.generic import TemplateView
from catalogue.models import Product
from sitemenu.models import MenuItems
from form.forms import *

class IndexView(TemplateView):

    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):

        context = {}
        context['last_products'] = Product.objects.filter(is_popular=True)
        context['page'] = MenuItems.objects.filter(is_index_page = True).first()
        context['contact_form'] = ContactForm()
        return context