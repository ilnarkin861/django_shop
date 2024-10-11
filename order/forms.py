from django import forms
from .models import Order
from regional_centers.models import City


class OrderForm(forms.ModelForm):
    class Meta:
        custom_error_messages = {}


    class Media:
        js = ('js/jquery.mask.min.js', 'js/mask-init.js', 'js/validator.js')


    name = forms.CharField(label=u'ФИО', widget=forms.TextInput(attrs={'class':'form-control', 'id':'checkuot-form-name', 'placeholder':u'Как к Вам обращаться?'}))
    email = forms.EmailField(label=u'Электронный адрес', widget=forms.TextInput(attrs={'class':'form-control', 'id':'checkuot-form-email', 'placeholder':u'Ваш электронный адрес'}))
    phone = forms.CharField(label=u'Телефон', widget=forms.TextInput(attrs={'class':'form-control', 'id':'checkuot-form-phone'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), label=u'Город', widget=forms.Select(attrs={'class':'form-control', 'id':'checkuot-form-city'}), empty_label=u'Выберите город из списка')
    address = forms.CharField(label=u'Адрес', widget=forms.TextInput(attrs={'class':'form-control', 'id':'checkuot-form-address', 'placeholder':u'Пример: ул. Ленина, 1, д. 2'}))
    note = forms.CharField(label=u'Заметки к заказу', required=False, widget=forms.Textarea(attrs={'class':'form-control', 'id':'checkuot-form-note', 'placeholder':u'Заметки к заказу'}))

    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'city', 'address', 'note',)


class OrderChangeForm(forms.Form):

    status = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=Order.STATES))

    class Meta:
        model = Order
        fields = ('status',)