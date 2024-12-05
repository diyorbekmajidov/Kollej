from rest_framework.views import APIView
from .serializers import *
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response

# Create your views here.

class Index(TemplateView):
    def get(self, request):
        news = News.objects.order_by("-date_created")[:4]
        context = {
            "news": news
        }
        return render(request, 'index.html', context)
        # return render(request, 'index.html')


class NewsView(APIView):
    def get(self, request):
        news = News.objects.order_by("-date_created")[:4]
        pass

class NewsHomeView(TemplateView):
    def get(self, request):
        news = News.objects.order_by("-date_created")[:4]
        context = {
            "news": news
        }
        return render(request, 'index.html', context)
        # return Response()