from django.db import models


class Phone(models.Model):
	# TODO: Добавьте требуемые поля
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, unique=True)
	price = models.IntegerField()
	image = models.ImageField()
	release_date = models.DateField()
	lte_exists = models.BooleanField()
	slug = models.SlugField()

	def __str__(self):
		return self.name
