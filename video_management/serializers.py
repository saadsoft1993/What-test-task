from rest_framework import serializers

from video_management.models import Video, Rating
from taggit.serializers import TagListSerializerField, TaggitSerializer


class VideoModelSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Video
        fields = ['id', 'name', 'url', 'tags', 'average_rating']


class RatingModelSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'video', 'rating']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data.update({'user': request.user})
        rating, created = Rating.objects.update_or_create(
            video=validated_data.get('video'),
            user=request.user,
            defaults={'rating': validated_data.get('rating')})
        return rating
