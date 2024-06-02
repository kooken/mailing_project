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
        fields = '__all__'

class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'

class AttemptForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Attempt
        fields = '__all__'
