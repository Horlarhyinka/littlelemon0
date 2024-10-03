from django.db import models
import uuid

def genUUid():
   return str(uuid.uuid4()).replace('-', '')[:8].upper()

# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)
   reference = models.CharField(max_length=8, default=genUUid, editable=False)
   def __str__(self):
      return self.first_name + ' ' + self.last_name
   
   def save(self, *args, **kwargs):
      if not self.reference:
         self.reference = genUUid()
      return super().save(*args, **kwargs)


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   menu_item_description = models.TextField(max_length=1000, default="")
   def __str__(self):
      return self.name