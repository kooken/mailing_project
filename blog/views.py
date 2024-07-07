from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, ListView

from blog.models import Blog


# Create your views here.
class BlogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    permission_required = 'blog.change_blogpost'
    fields = ('title', 'content', 'preview',)


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        blogpost = form.save()
        user = self.request.user
        blogpost.owner = user
        blogpost.save()
        return super().form_valid(form)

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        return Blog.objects.filter(product=Blog.objects.get(pk=self.kwargs.get('pk')))