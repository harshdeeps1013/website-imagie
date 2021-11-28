from django.db import models

class image_data(models.Model):

   image_id = models.AutoField(primary_key = True) 
   likes = models.IntegerField(default=0)
   name=models.CharField(max_length = 50)
   submitted_by=models.CharField(max_length = 70,default="ME")
   alt=models.CharField(max_length = 70,default="image")

   #class Meta:
     # db_table = "Image_data"


class Document(models.Model):
    description = models.CharField(max_length=255,)
    image = models.FileField(upload_to='project1/static/project1/images')