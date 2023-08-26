from django.db import models
from medias import utils
from django.db.models import Avg


class Category(models.Model):
    name = models.CharField('Nombre', max_length=100)

    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.CharField('Nombre', max_length=255)
    categories = models.ManyToManyField(Category, verbose_name='Genero', related_name='medias')
    type =  models.CharField('Tipo', max_length=50, choices=utils.TYPE_OF_MEDIA)

    @property
    def number_of_views(self):
      return self.viewer_media.filter(media=self, has_watched=True).count()

    @property
    def rating(self):
        avg_rating = self.viewer_media.filter(media=self, has_watched=True).aggregate(Avg('rating'))['rating__avg']
        return avg_rating if avg_rating is not None else 0

    def __str__(self):
        return self.name