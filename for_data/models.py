from django.db import models

# Create your models here.
class Verse(models.Model):
	book = models.IntegerField()
	chapter = models.IntegerField()
	verse = models.IntegerField()
	content = models.CharField(max_length=600)

	def __str__(self):
		text = self.content
		if (len(text) > 100):
			text = text[:100]  + '. . . .'
		return text

class LinkType(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return self.name

class Link(models.Model):
  from_verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name='link_from_verse')
  to_verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name='link_to_verse')
  link_type = models.ForeignKey(LinkType, on_delete=models.CASCADE)