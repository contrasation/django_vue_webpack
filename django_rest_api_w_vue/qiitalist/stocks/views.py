from django.shortcuts import render
from django.conf import settings
# from django.http.response import HttpResponse
from rest_framework import viewsets

import os

from .models import Stock
from .serializers import StockSerializer

# Create your views here.


def index(request):
    return render(request, 'stocks/vue_grid.html')


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_fields = ("id", "title", 'stock_count')