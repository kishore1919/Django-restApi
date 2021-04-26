from django.urls import path
from .views import SongsApi,SongsCreateApi,SongsUpdateApi#,SongsDeleteApi

urlpatterns = [
    path('list/',SongsApi.as_view()),
    path('',SongsCreateApi.as_view()),
    path('<int:pk>/',SongsUpdateApi.as_view()),
    #path('delete/<int:pk>/',SongsDeleteApi.as_view()),
]

