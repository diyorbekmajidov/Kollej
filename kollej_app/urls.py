from django.urls import path 
from .views import Index, NewsView, EventView, NewById, Directions, Requisitesview,LibraryViews, TtjViews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', Index.as_view()),
    path('yangiliklar/', NewsView, name='news_list'),
    path('events/', EventView, name='events_list'),
    path('yangilik/<int:pk>/', NewById, name='news_by_id'),
    path('directions/<int:pk>/', Directions, name="directions_list"),
    path('contact/', Requisitesview.as_view()),
    path('library/', LibraryViews.as_view()),
    path('ttj/', TtjViews.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)