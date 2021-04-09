from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ManyToManyField('Category', blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(max_length=750)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product/%y/%m/%d', blank=True, null=True)
    available = models.BooleanField(default=True)
    objects = models.Manager()
    available_products = ProductManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategories', blank=True,
                                     null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_sub = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_filter', args=[self.slug, ])
