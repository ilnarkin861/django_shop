from django import forms





class ContactForm(forms.Form):
    custom_error_messages = {
        'name': {
            'error_messages': {
                'required': u'Поле Имя не должно быть пустым'
            }
        },

        'email': {
            'error_messages': {
                'required': u'Поле Электронный адрес не должно быть пустым',
                'invalid': u'Электронный адрес заполнен неверно'
            }
        },

        'message': {
            'error_messages': {
                'required': u'Поле Сообщение не должно быть пустым'
            }
        },

    }




    class Media:
        js = ('js/validator.js', 'js/form-ajax.js')



    name = forms.CharField(label=u'Имя', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':u'Как к Вам обращаться?', 'id':'form-name'}), error_messages=custom_error_messages['name']['error_messages'])
    email = forms.EmailField(label=u'Электронный адрес', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':u'Ваш электронный адрес', 'id':'form-email'}), error_messages=custom_error_messages['email']['error_messages'])
    message = forms.CharField(label=u'Сообщение', widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':u'Напишите ваше сообщение', 'id':'form-message'}), error_messages=custom_error_messages['message']['error_messages'])


class RegistrationPhoneForm(forms.Form):

    class Media:
        js = ('js/validator.js', 'js/jquery.mask.min.js', 'js/mask-init.js', 'js/form-ajax.js')


    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-lg reg-phone-input'}))
