from django.shortcuts import render
from django.views import View
from .models import Post, Comment, Users
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


"""
Views for the feed, listing all existing posts that been created,
and a form to create new posts for the feed.
"""
class PostList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_feed': posts,
            'form': form,
        }

        return render(request, 'post_feed.html', context)


    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            add_post = form.save(commit=False)
            add_post.author = request.user
            add_post.save()

        context = {
            'post_feed': posts,
            'form': form,
        }

        return render(request, 'post_feed.html', context)


"""
Views for the posts detail, when user click on a post in the feed,
they see the post on its own and can comment, edit and delete comments,
or edit and delete the post if its created by the user.
"""
class PostDetail(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
    
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'post_detail.html', context)
        
    """
    Add a new comment to the post
    """
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        if form.is_valid():
            add_comment = form.save(commit=False)
            add_comment.author = request.user
            add_comment.post = post
            add_comment.save()

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
        return render(request, 'post_detail.html', context)


"""
Views for edit a uploaded post, and using get_successs_url to rederict back
to the post detail template when user has submit the edit.
"""
class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['body']
    template_name = 'post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={'pk':pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


"""
Views for Delete a uploaded (by user) post from the feed.
"""
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_feed')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


"""
Views for Delete a uploaded (by user) comment from the feed.
"""
class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post_detail', kwargs={'pk': pk})
        
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class UserProfile(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Users.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts
        }

        return render(request, 'user_profile.html', context)


class UserProfileEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Users
    fields = ['picture', 'name', 'location', 'birthday', 'gender', 'bio']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.use