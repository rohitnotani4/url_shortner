from django.db import models

# Create your models here.
class Url_db(models.Model):
    long_url=models.URLField(max_length=2000)
    unique_id=models.CharField(max_length=6, primary_key=True)
    short_url=models.CharField(max_length=50)


    def  __unicode__(self):
        return self.long_url
