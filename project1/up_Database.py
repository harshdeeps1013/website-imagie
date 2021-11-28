from project1.models import image_data
import os

def update_image_model():
    lo = os.listdir("C:\\Users\\DELL\\websitep\\project1\\static\\project1\\images")
    for s in lo:
        new=image_data.objects.create(name=s,alt=s,submitted_by="MEE")
        new.save()  