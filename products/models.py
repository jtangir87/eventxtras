from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def is_active(self):
        return self.active == True

class CategoryFilter(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True, related_name="fitlers")
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category Filter"
        verbose_name_plural = "Category Filters"

    def __str__(self):
        return "{} - {}".format(self.category.name, self.name)

def product_default_images(instance, filename):
    upload_path = "products/default_image"
    return os.path.join(upload_path, filename.lower())

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True)
    cat_filter = models.ManyToManyField(CategoryFilter)
    description = models.TextField()
    list_order = models.PositiveIntegerField()
    primary_image = models.ImageField(upload_to=product_default_images)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('list_order',)


def product_extra_images(instance, filename):
    upload_path = "products/extra_images"
    return os.path.join(upload_path, filename.lower())

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_extra_images)

    def __str__(self):
        return "{} - {}".format(self.product.name, self.id)
