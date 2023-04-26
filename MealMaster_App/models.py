from django.db import models

class MonImage(models.Model):

    image = models.ImageField(upload_to='images/')
    name = models.TextField(max_length=500, default="")
    description = models.TextField(max_length=800, default="")

    def __str__(self):
        return f"{self.image.name}"

class tag(models.Model):


    tag = models.TextField(max_length=500, default="")


    def __str__(self):
        return f"{self.tag}"