from endless_pagination.views import AjaxListView
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Post, Poem, Letter


class PostListView(AjaxListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context


class PoemListView(ListView):
    model = Poem
    queryset = Poem.objects.all()
    context_object_name = "poems"

    def get_context_data(self, **kwargs):
        context = super(PoemListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PoemDetailView(DetailView):
    model = Poem

    def get_context_data(self, **kwargs):
        context = super(PoemDetailView, self).get_context_data(**kwargs)
        context['poems'] = Poem.objects.all()
        return context


class LetterListView(ListView):
    model = Letter
    queryset = Letter.objects.all()
    context_object_name = "letters"

    def get_context_data(self, **kwargs):
        context = super(LetterListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class LetterDetailView(DetailView):
    model = Letter

    def get_context_data(self, **kwargs):
        context = super(LetterDetailView, self).get_context_data(**kwargs)
        context['letters'] = Letter.objects.all()
        return context
