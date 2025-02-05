from django.urls import path 
from django.conf.urls.i18n import i18n_patterns
from .views import (Index,
             NewsView, EventView, NewById,
            Directions, Requisitesview,LibraryViews, 
            TtjViews,Leadershipview,Opendata,
            Charter,DocumetById,PetitionsView, test_language_view, VedioNewsView
            )
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('test_language/', test_language_view, name='test_language'),
    path('', Index.as_view()),
    path('yangiliklar/', NewsView, name='news_list'),
    path('events/', EventView, name='events_list'),
    path('yangilik/<int:pk>/', NewById, name='news_by_id'),
    path('video-gallery/', VedioNewsView.as_view()),
    path('video-gallery/<int:pk>/', VedioNewsView.as_view()),
    path('directions/<int:pk>/', Directions, name="directions_list"),
    path('contact/', Requisitesview.as_view()),
    path('library/', LibraryViews.as_view(), name='libary'),
    path('ttj/', TtjViews.as_view()),
    path('rahbariyat/', Leadershipview.as_view()),
    path('opendata/', Opendata, name='ochiq malumotlar'),
    path('charter/', Charter, name="nizom"),
    path('documet/<int:pk>/', DocumetById, name='opendata_charter_byid'),
    path('submit-petition/', PetitionsView.as_view(), name='submit_petition'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

