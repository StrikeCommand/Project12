from django.db import models


class Point(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, related_name='points')

    class Meta:
        unique_together = ('name', 'city')

    def __str__(self):
        return '{} ({})'.format(self.name, self.city.name)

    def __repr__(self):
        return 'Point({}, {}, {}, {})'.format(
            self.name, self.latitude, self.longitude, self.city.name)


class PointImage(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='images')

    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return u'Image {} of {}'.format(self.pk, self.point.name)

    def __repr__(self):
        return u'PointImage({}, {})'.format(self.point.name, self.url)


class City(models.Model):

    name = models.CharField(max_length=100)

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'City({}, {}, {})'.format(self.name, self.latitude, self.longitude)
