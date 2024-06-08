from home.models import Post, TripFile
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.views.decorators.http import require_GET



from home.forms import TripFileForm
class IndexView(ListView):
    queryset = Post.objects.all()
    template_name = "index.html"
    context_object_name = "posts"
    ordering = ["-created"]


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "create_view.html"
    success_url = reverse_lazy("home_page")


class FileUploadView(FormView):
    template_name = 'upload.html'
    success_url = reverse_lazy("home_page")
    form_class = TripFileForm

    def form_valid(self, form):
        form.save()
        
        return super().form_valid(form)
    
# @require_GET
# def load_gtfs(request):
#     trip_files = TripFile.objects.all()
#     return JsonResponse({"files": [file.file.url for file in trip_files]})