from django.db import models

class Foo(models.Model):
	name = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='photos')
	score = models.FloatField(default=0)
	added_date = models.DateTimeField(auto_now_add=True)
	categor = models.ForeignKey('Category')

	def __unicode__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'