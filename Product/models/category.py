from django.db import models

class Categor(models.Model):
    title = models.CharField(max_length=60, blank = True)

    def __str__(self):
        return self.title
