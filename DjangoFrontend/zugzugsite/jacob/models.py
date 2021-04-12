from django.db import models

# Create your models here.
class Image(models.Model):
    anime_id = models.IntegerField(primary_key = True)
    image_medium = models.CharField(max_length=255)
    image_large = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'Image'

class Studio(models.Model):
    studio_id = models.IntegerField()
    studio_name = models.CharField(max_length=40)

class A2S(models.Model):
    studio_id = models.IntegerField()
    anime_id = models.IntegerField()


