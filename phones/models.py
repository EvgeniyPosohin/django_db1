from django.db import models
from django.utils import timezone


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='uploads/')
    price = models.IntegerField(default=0)
    release_date = models.DateField(auto_now_add=False)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=30)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.image},' \
               f' {self.release_date}, {self.price}, {self.lte_exists},' \
               f'{self.slug}'
