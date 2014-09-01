from django.db import models

# Create your models here.


class Feed(models.Model):
	name = models.CharField(max_length=50)
	url = models.URLField()

	def __unicode__(self):
		return self.name
		