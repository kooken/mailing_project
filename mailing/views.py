from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import ClientForm, MailingForm, MessageForm, AttemptForm
from mailing.models import Client, Message, Mailing, Attempt


# Create your views here.
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    success_url = reverse_lazy('mailing:index')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:index')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:index')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:index')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'message_list.html'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    def form_valid(self, form):
        message_owner = form.save()
        user = self.request.user
        message_owner.owner = user
        message_owner.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailing_list.html'


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        mailing_owner = form.save()
        user = self.request.user
        mailing_owner.owner = user
        mailing_owner.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


# class AttemptListView(LoginRequiredMixin, ListView):
#     model = Attempt
#     template_name = 'attempt_list.html'
#
#
# class AttemptDetailView(LoginRequiredMixin, DetailView):
#     model = Attempt
#     success_url = reverse_lazy('mailing:index')


class AttemptCreateView(LoginRequiredMixin, CreateView):
    model = Attempt
    form_class = AttemptForm
    success_url = reverse_lazy('mailing:index')

    def form_valid(self, form):
        attempt_owner = form.save()
        user = self.request.user
        attempt_owner.owner = user
        attempt_owner.save()
        return super().form_valid(form)
#
#
# class AttemptUpdateView(LoginRequiredMixin, UpdateView):
#     model = Attempt
#     form_class = AttemptForm
#     success_url = reverse_lazy('mailing:index')
#
#
# class AttemptDeleteView(LoginRequiredMixin, DeleteView):
#     model = Attempt
#     success_url = reverse_lazy('mailing:index')