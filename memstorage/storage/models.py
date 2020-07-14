from django.db import models

# Create your models here.

class tag(models.Model):
	text = models.CharField(max_length=20, help_text="name tag")
	def __str__(self):
		return self.text

class mem(models.Model):
	link = models.CharField(max_length=20, help_text="link to mem")
	text = models.CharField(max_length=200, help_text="text mem")
	date = models.DateTimeField()
	tags = models.ManyToManyField(tag, help_text="tags mem")

	def __str__(self):
		return self.text
	
	def get_absolute_url(self):
	    return reverse('model-detail-view', args=[str(self.id)])
