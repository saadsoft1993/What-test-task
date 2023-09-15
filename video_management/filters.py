import django_filters
from video_management.models import Video


class VideoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    url = django_filters.CharFilter(field_name='url', lookup_expr='icontains')
    average_rating__gte = django_filters.NumberFilter(field_name='average_rating', lookup_expr='gte')
    average_rating__lte = django_filters.NumberFilter(field_name='average_rating', lookup_expr='lte')

    class Meta:
        model = Video
        fields = ['name', 'url', 'average_rating__gte', 'average_rating__lte']