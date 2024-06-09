from home.models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .ParserGTFS import ParserGTFS
from django.shortcuts import render



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
        trip_file_instance = form.save()
        ParserGTFS(trip_file_instance.file.path).parse()
        return super().form_valid(form)    
  
def stops_for_route(request, route_id):
    trips = Trips.objects.filter(route_id=route_id).values_list('trip_id', flat=True)
    
    stop_times = StopTimes.objects.filter(trip_id__in=trips).order_by('stop_sequence')
    
    stop_ids = stop_times.values_list('stop_id', flat=True).distinct()
    stops = Stops.objects.filter(stop_id__in=stop_ids)
    stops_list = list(stops.values('stop_id', 'stop_name', 'stop_lat', 'stop_lon'))
    
    return JsonResponse(stops_list, safe=False)
    
def shape_for_route(request, route_id):
    trips = Trips.objects.filter(route_id=route_id).values_list('trip_id', flat=True)
    shape_ids = trips.values_list('shape_id', flat=True).distinct()
    
    shapes = Shapes.objects.filter(shape_id__in=shape_ids).order_by('shape_id', 'shape_pt_sequence')
    shapes_data = []
    for shape in shapes:
        shapes_data.append({
            'shape_id': shape.shape_id,
            'shape_pt_lat': shape.shape_pt_lat,
            'shape_pt_lon': shape.shape_pt_lon,
            'shape_pt_sequence': shape.shape_pt_sequence
        })
    
    return JsonResponse(shapes_data, safe=False)


def routes_for_stop(request, stop_id):
    try:
        stop_times = StopTimes.objects.filter(stop_id=stop_id)
        unique_route_ids = stop_times.values_list('trip_id', flat=True).distinct()
        return JsonResponse(list(unique_route_ids), safe=False)
    except Stops.DoesNotExist:
        return JsonResponse({'error': 'Stop not found'}, status=404)

