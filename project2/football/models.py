from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'category'
    def __str__(self):
        return self.name

class Socccer(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='football/',blank=True,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    class Meta:
        db_table ='soccer'

    def __str__(self):
        return f'{self.name}'
    