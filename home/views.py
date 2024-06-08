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


def transfers_json(request):
    transfers = Transfers.objects.all()
    transfer_data = []
    for transfer in transfers:
        from_stop = Stops.objects.filter(stop_id=transfer.from_stop_id).first()
        to_stop = Stops.objects.filter(stop_id=transfer.to_stop_id).first()
        if from_stop and to_stop:
            transfer_data.append({
                'from_stop': {
                    'id': from_stop.stop_id,
                    'lat': from_stop.stop_lat,
                    'lon': from_stop.stop_lon,
                    'name': from_stop.stop_name
                },
                'to_stop': {
                    'id': to_stop.stop_id,
                    'lat': to_stop.stop_lat,
                    'lon': to_stop.stop_lon,
                    'name': to_stop.stop_name
                },
                'transfer_type': transfer.transfer_type,
                'min_transfer_time': transfer.min_transfer_time
            })
    return JsonResponse(transfer_data, safe=False)
