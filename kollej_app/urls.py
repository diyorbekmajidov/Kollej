from django.urls import path 
from .views import Index, NewsView, EventView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', Index.as_view()),
    path('yangiliklar/', NewsView, name='news_list'),
    path('events', EventView, name='events_list')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)