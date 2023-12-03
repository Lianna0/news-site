from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta:
        abstract = True


class Category(TimeStampModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(unique=True, max_length=50)
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class News(TimeStampModel):
    maincategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Categories')
    slug = models.SlugField(unique=True)
    additional_category = models.ManyToManyField(Category, blank=True)
    description = models.TextField()
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/')
    short_text = models.CharField(max_length=250)
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title





