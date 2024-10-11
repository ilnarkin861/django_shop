from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from .models import MenuItems
from form.forms import *
from regional_centers.models import CenterInfo


class StaticPagesView(TemplateView):
    default_template_name = 'default.html'

    def get(self, request, *args, **kwargs):


        try:

            page = MenuItems.objects.get(url = kwargs['page_url'])
            context ={}
            context['page'] = page
            context['contact_form'] = ContactForm
            context['reg_form'] = RegistrationPhoneForm

            if page.is_delivery_link:
                context['centers'] = CenterInfo.objects.all()

            if page.page_template_name:
                template = page.page_template_name
            else:
                template = self.default_template_name


            return render(request, 'sitemenu/'+template, context )
        except ObjectDoesNotExist:
            return render(request, '404.html', status=404)