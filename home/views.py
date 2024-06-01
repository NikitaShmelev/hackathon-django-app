# myapp/views.py

from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello, this is the index page of myapp.")


# myapp/views.py

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
