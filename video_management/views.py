from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView

from video_management.filters import VideoFilter
from video_management.models import Video, Rating
from video_management.serializers import VideoModelSerializer, RatingModelSerializer


class VideoListAPIView(ListAPIView):
    queryset = Video.objects.annotate(averaging_rating=Avg("rating__rating")).all()
    serializer_class = VideoModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = VideoFilter
    ordering_fields = ['name', 'url']


class VideoDetailAPIView(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoModelSerializer


class VideoDestroyAPIView(DestroyAPIView):
    queryset = Video.objects.all()


class RatingCreateAPIView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer
