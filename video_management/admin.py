from django.contrib import admin

from video_management.models import Video, Rating


class VideoModelAdmin(admin.ModelAdmin):

    list_display = ['name', 'url', 'tags_list', 'created_at', 'updated_at']
    search_fields = ['name', 'url']

    def tags_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class RatingModelAdmin(admin.ModelAdmin):

    list_display = ['user', 'video', 'rating', 'created_at', 'updated_at']
    search_fields = ['user', 'video']
    autocomplete_fields = ['user', 'video']


admin.site.register(Video, VideoModelAdmin)
admin.site.register(Rating, RatingModelAdmin)
