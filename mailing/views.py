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
    success_url = reverse_lazy('mailing:index')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:index')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:index')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:index')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mailing_list.html'


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    success_url = reverse_lazy('mailing:index')


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:index')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:index')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:index')


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