from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Dan Brown')
    category = models.ForeignKey(
        Category, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20)
    pages = models.PositiveIntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField(max_length=500)
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imageUrl = models.URLField(max_length=500)
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.product_tag + ' ' + self.name
