from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import (ClientListView, ClientDetailView, ClientDeleteView, ClientCreateView, ClientUpdateView,
                           MessageCreateView, MessageDeleteView, MessageDetailView, MessageUpdateView, MessageListView,
                           MailingListView, MailingCreateView, MailingDeleteView, MailingDetailView, MailingUpdateView,
                           AttemptCreateView, AttemptListView, main_page)

app_name = MailingConfig.name

urlpatterns = [
    path('main', main_page, name='main_page'),

    path('', ClientListView.as_view(), name='index'),
    path('client_detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('edit_client/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),

    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('update_message/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('message_list/', MessageListView.as_view(), name='message_list'),

    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('mailing_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),

    path('create_attempt/', AttemptCreateView.as_view(), name='create_attempt'),
    path('attempt_list/', AttemptListView.as_view(), name='attempt_list'),
]
