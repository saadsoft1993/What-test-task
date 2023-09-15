from django.urls import path

from video_management.views import VideoListAPIView, VideoDetailAPIView, RatingCreateAPIView

urlpatterns = [
    path('videos/', VideoListAPIView.as_view(), name='video_list'),
    path('videos/<str:pk>/', VideoDetailAPIView.as_view(), name='video_detail'),
    path('video_rating/', RatingCreateAPIView.as_view(), name='video_rating'),
]