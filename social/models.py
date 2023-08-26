from django.db import models
from django.contrib.auth.models import User
from medias.models import Media
from django.core.validators import MaxValueValidator, MinValueValidator



class Viewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Espectador', related_name='viewer')
    watched_medias = models.ManyToManyField(Media, through='ViewerMedia')

    def __str__(self):
        return self.user.username


class ViewerMedia(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='viewer_media')
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    has_watched = models.BooleanField(default=False)

    class Meta:
        unique_together = ('viewer', 'media')
