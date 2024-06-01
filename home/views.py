from django.views.generic import TemplateView
from home.models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PostForm



# myapp/views.py

from django.views.generic import ListView

class IndexView(ListView):
    # filter_set =
    queryset = Post.objects.all()
    template_name = "index.html"
    context_object_name = 'posts'  # Specify the context variable name to use in the template
    ordering = ['-created']  # Optionally specify the ordering of objects


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "create_view.html"
    success_url = reverse_lazy("home_page")
