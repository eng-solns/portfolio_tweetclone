from django.urls import path
from tweets import views as tweets_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', tutorials_views.index, name='home'),
    path('', tweets_views.index.as_view(), name='home'),
    path('api/tutorials/', tweets_views.tweet_list),
    path('api/tutorials/<int:pk>/', tweets_views.tweet_detail),
    path('api/tutorials/published/', tweets_views.tweet_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)