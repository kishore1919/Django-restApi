from django.urls import path
from .views import AudiobookApi,AudiobookCreateApi,AudiobookUpdateApi#,AudiobookDeleteApi

urlpatterns = [
    path('list/',AudiobookApi.as_view()),
    path('',AudiobookCreateApi.as_view()),
    path('<int:pk>',AudiobookUpdateApi.as_view()),
]

