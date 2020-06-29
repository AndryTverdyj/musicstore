from django.db import models
from django.contrib.postgres.fields import ArrayField


#  The Model for all records saving
class MusicWork(models.Model):
    iswc = models.CharField(max_length=20, unique=True, null=True, blank=True)
    title = models.CharField(max_length=250)
    contributors = ArrayField(models.CharField(max_length=100))
    class Meta:
        ordering = ['iswc']

    def __str__(self):
        return f"{self.iswc}-{self.title}"

# The Model for uploading .csv-files 
class MusicWorkFile(models.Model):
    upload_file = models.FileField(upload_to='work_files')
