from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse
from .serializers import *
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response


class Index(TemplateView):
    def get(self, request):
        news = News.objects.order_by("-date_created")[:4]
        event = News.objects.filter(new_type=2)[:4]
        directions = DirectionsModel.objects.all()
        context = {
            "news": news,
            "events":event,
            "directions":directions
        }
        return render(request, 'index.html', context)


def NewsView(request):
    object_all = News.objects.filter(new_type="1").order_by('-date_created')
    page_num = request.GET.get('page', 1)
    print(object_all.count())

    paginator = Paginator(object_all, 9) 

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'news.html', {'page_obj': page_obj})

def EventView(request):
    object_all = News.objects.filter(new_type=2)
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

def Directions(request, pk):
    if not pk:

        directions = DirectionsModel.objects.all()
        context = {"directions":directions}
        return render(request, '.html', context) #this code return all directions
    direction = DirectionsModel.objects.get(pk=pk)
    context_id = {"directionby_id":direction}
    return  render(request, 'directions-single.html', context_id) #this code return by id directions

class Requisitesview(TemplateView):
    def get(self, request):
        requisites = Requisites.objects.last()
        serializers = RequisitesSerializers(requisites)
        return render(request, 'contact.html',{"data":serializers.data})
    

class Leadershipview(TemplateView):
    def get(self, request):
        leader = Leadership.objects.all()
        serializers = LeadershipSerializers(leader, many=True)
        return render(request, '.html', {"data":serializers.data})
    
class LibraryViews(TemplateView):
    template_name = "library.html"

class TtjViews(TemplateView):
    template_name = "ttj.html"