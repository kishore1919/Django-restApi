from django.urls import path
from .views import PodcastApi,PodcastCreateApi,PodcastUpdateApi#,PodcastDeleteApi

urlpatterns = [
    path('list/',PodcastApi.as_view()),
    path('',PodcastCreateApi.as_view()),
    path('<int:pk>',PodcastUpdateApi.as_view()),
   # path('delete/<int:pk>/',PodcastDeleteApi.as_view()),
]

