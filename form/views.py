from smtplib import SMTPException
from django.http import JsonResponse
from django.views.generic import FormView
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import *
from .mixin import AjaxableResponseMixin
from ivangreenway.email_utils import contacts

class ContactFormView(AjaxableResponseMixin, FormView):

    form_class = ContactForm
    template_name = 'base.html'
    success_url = '/'



    def form_valid(self, form):

        try:
            email_body = contacts(form.cleaned_data)
            email = EmailMultiAlternatives(u'Сообщение с сайта', email_body, settings.EMAIL_HOST_USER, settings.EMAIL_LIST)
            email.attach_alternative(email_body, "text/html")
            email.send()
            return super().form_valid(form, json_data={'message':u'Ваше сообщение успешно отправлено'})
        except SMTPException:
            return JsonResponse({'message': u'Ошибка при отправке сообщения. Попробуйте еще раз'}, status=400)




class PartnerRegistrationView(AjaxableResponseMixin, FormView):

    form_class = RegistrationPhoneForm
    template_name = 'sitemenu/business.html'
    success_url = '/business'

    def form_valid(self, form):
        try:
            email = EmailMultiAlternatives(u'Запрос на регистрацию', 'Номер телефона: '+form.cleaned_data['phone'], settings.EMAIL_HOST_USER, settings.EMAIL_LIST)
            email.send()
            return super().form_valid(form, json_data={'message': u'Ваш запрос на регистрацию успешно отправлен. В ближайшее время мы отправим вам нашу инвайт ссылку.'})
        except SMTPException:
            return JsonResponse({'message': u'Ошибка при отправке сообщения. Попробуйте еще раз'}, status=400)


