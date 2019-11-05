from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import WorldBorder


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


def county_datasets(request):
    counties = serialize('geojson', WorldBorder.objects.all())
    return HttpResponse(counties, content_type='json')
