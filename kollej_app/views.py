from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse
from .serializers import *
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import get_language

def test_language_view(request):
    current_language = get_language()
    return HttpResponse(f"Current language is: {current_language}")



class Index(TemplateView):
    def get(self, request):
        news = News.objects.order_by("-date_created")[:4]
        event = News.objects.filter(new_type=2)[:4]
        directions = DirectionsModel.objects.all()
        regularlyquestion = RegularlyQuestion.objects.all()
        context = {
            "news": news,
            "events":event,
            "directions":directions,
            "questions":regularlyquestion
        }
        return render(request, 'index.html', context)


def NewsView(request):
    object_all = News.objects.filter(new_type="1").order_by('-date_created')
    page_num = request.GET.get('page', 1)
    print(object_all.count())

    paginator = Paginator(object_all, 5) 

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

    paginator = Paginator(object_all, 5) 

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'events.html', {'page_obj': page_obj})

def NewById(request, pk):
    newsbyid = News.objects.get(id=pk)
    context = {"newsbyid":newsbyid}
    return render(request, 'news-single.html', context)


class VedioNewsView(TemplateView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                video = Vedio_New.objects.get(id=pk)
                views = video.views+1
                video.views = views
                video.save()
                lastest = Vedio_New.objects.order_by("-id")[:5]
                lastest_serializer = VedioNewSerializer(lastest, many=True)

                print("VIDEO:", video)
                print("LASTEST:", lastest_serializer.data)
                return render(
                    request,
                    'video-gallery-item.html', 
                    {
                        "vedio_news":video,
                        "lastest":lastest_serializer.data
                    }
                )
            except Exception as e:
                print(e)
                return render(request,'video-gallery-item.html') 

        try:
            vedio_news = Vedio_New.objects.all().order_by("date_created")[::-1]
            page = Paginator(vedio_news, 9)
            page_num = int(request.GET.get('page', 1))
            return render(request,'video-gallery.html', {"page_obj":page.page(page_num)})
        except Exception as e:
            print(e)
            return render(request,'video-gallery.html')

def Opendata(request):
    open_data = OpenData.objects.filter(open_method = 1)
    context = {"open_data":open_data}
    return render(request, 'open-data.html', context)

def Charter(request):
    charter = OpenData.objects.filter(open_method = 2)
    context = {"charter":charter}
    return render(request, 'charter.html', context)

def DocumetById(request, pk):
    documet = OpenData.objects.get(id=pk)
    context = {"documentbyid":documet}
    return render(request, '.html', context)

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
        return render(request, 'leadership.html', {"data":serializers.data})
    

class PetitionsView(APIView):
    def post(self, request):
        serializers = PetitionSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class LibraryViews(TemplateView):
    template_name = "library.html"

class TtjViews(TemplateView):
    template_name = "ttj.html"