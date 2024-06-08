from home.models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import ListView
from django.views.generic.edit import FormView

from home.forms import TripFileForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .ParserGTFS import ParserGTFS
import pdb



from home.forms import TripFileForm
class IndexView(ListView):
    queryset = Post.objects.all()
    template_name = "index.html"
    context_object_name = "posts"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "create_view.html"
    success_url = reverse_lazy("home_page")


class FileUploadView(FormView):
    template_name = "upload.html"
    print("FileUploadView")
    template_name = 'upload.html'
    success_url = reverse_lazy("home_page")
    form_class = TripFileForm

    def form_valid(self, form):
        trip_file_instance = form.save()
        ParserGTFS(trip_file_instance.file.path).parse()
        return JsonResponse({"status": "success"})


from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import JsonResponse
from home.models import Shapes, Stops


class ShapeMapView(TemplateView):
    template_name = "shape_map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["shapes"] = serialize("json", Shapes.objects.all())
        context["stops"] = serialize("json", Stops.objects.all())
        return context


def shapes_json(request):
    shapes = Shapes.objects.all()
    data = serialize("json", shapes)
    return JsonResponse(data, safe=False)


def stops_json(request):
    stops = Stops.objects.all()
    data = serialize("json", stops)
    return JsonResponse(data, safe=False)
class TransferMapView(TemplateView):
    template_name = 'transfer_map.html'

def stops_near_location(request):
    # Get bounds from the request
    north_east_lat = float(request.GET.get("north_east_lat"))
    north_east_lon = float(request.GET.get("north_east_lon"))
    south_west_lat = float(request.GET.get("south_west_lat"))
    south_west_lon = float(request.GET.get("south_west_lon"))

    # Filter stops within the bounds
    stops_within_bounds = Stops.objects.filter(
        stop_lat__lte=north_east_lat,
        stop_lat__gte=south_west_lat,
        stop_lon__lte=north_east_lon,
        stop_lon__gte=south_west_lon,
    )

    stops_data = []
    for stop in stops_within_bounds:
        stops_data.append({
            'id': stop.stop_id,
            'name': stop.stop_name,
            'lat': stop.stop_lat,
            'lon': stop.stop_lon,
        })

    return JsonResponse(stops_data, safe=False)