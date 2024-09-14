from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog
from mailing.forms import ClientForm, MailingForm, MessageForm, AttemptForm
from mailing.models import Client, Message, Mailing, Attempt


def main_page(request):
    context = {"count_mailing_items": Mailing.objects.all().count(),
               "count_active_mailing_items": Mailing.objects.filter(mailing_status='started').count(),
               "count_unique_clients": Client.objects.values_list('email', flat=True).count(),
               "random_blogs": Blog.objects.order_by('?')[:3]}
    return render(request, 'mailing/index.html', context=context)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

    def get_queryset(self):
        client_list = super().get_queryset().filter(owner=self.request.user)
        return client_list


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

    def get_queryset(self):
        client_list = super().get_queryset().filter(owner=self.request.user)
        return client_list


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

    def get_queryset(self):
        return super().get_queryset().filter(mailing_owner=self.request.user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.mailing_owner = user
        mailing.save()
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


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    template_name = 'attempt_list.html'


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
