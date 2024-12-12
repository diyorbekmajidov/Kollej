from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse
from .serializers import *
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response

# Create your views here.

class Index(TemplateView):
    def get(self, request):
        news = News.objects.order_by("-date_created")[:4]
        event = News.objects.filter(new_type=2)[:4]
        context = {
            "news": news,
            "events":event
        }
        return render(request, 'index.html', context)


def NewsView(request):
    object_all = News.objects.filter(new_type="news")
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_all, 9) 

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'page_obj': page_obj})

def EventView(request):
    object_all = News.objects.filter(new_type="events")
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_all, 9) 

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'evets.html', {'page_obj': page_obj})

def NewById(request, pk):
    newsbyid = News.objects.get(id=pk)
    context = {"newsbyid":newsbyid}
    return render(request, 'news-single.html', context)
