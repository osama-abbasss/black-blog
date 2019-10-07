from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from . import forms
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView,
                                  DetailView, TemplateView)


class About(TemplateView):
    template_name = 'posts/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(active=True).order_by('-created')


class PostDetailView(DetailView):
    model = Post


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = forms.PostForm
    login_url = '/login/'
    redirect_field_name = 'post/post_detail.html'


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = forms.PostEditForm
    template_name = 'posts/post_update.html'
    login_url = '/login/'


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')



####################################################

""""""""""""""""" For Comments """""""""""""""""""""

####################################################


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:post_detail', pk=pk)
        
    else:
        form = forms.CommentForm
        
    context = {'form': form}
    
    return render(request, 'posts/comment_form.html', context)