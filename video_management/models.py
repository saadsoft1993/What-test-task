import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

User = get_user_model()


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class VideoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(average_rating=models.Avg("rating__rating"))


class Video(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    url = models.URLField()
    name = models.CharField(max_length=255)
    tags = TaggableManager(through=UUIDTaggedItem)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = VideoManager()

    def __str__(self):
        return self.name


class Rating(models.Model):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

    RATING_CHOICE = (
        (ONE_STAR, "1"),
        (TWO_STAR, "2"),
        (THREE_STAR, "3"),
        (FOUR_STAR, "4"),
        (FIVE_STAR, "5"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING_CHOICE)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ["user", "video"]

    def __str__(self):
        return f"{self.user} {self.video} {self.rating}"
