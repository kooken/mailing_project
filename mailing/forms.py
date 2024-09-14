from django import forms
from mailing.models import Client, Mailing, Message, Attempt


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'active_version':
                field.widget.attrs['class'] = ' form-check-input'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ("mailing_owner",)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['mailing_clients'].queryset = Client.objects.filter(owner=user)
        self.fields['mailing_message'].queryset = Message.objects.filter(owner=user)


class AttemptForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Attempt
        fields = '__all__'
