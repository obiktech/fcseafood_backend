from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=90)
    category_slogan = models.CharField(max_length=40)
    category_img = models.ImageField(upload_to="assets")


    def __str__(self):
        return self.category_name
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=40)
    subcategory_img = models.ImageField(upload_to="assets")


    def __str__(self):
        return self.subcategory_name
    

class Product(models.Model):
    product_sku = models.CharField(max_length=30)
    product_name = models.CharField(max_length=150)
    product_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    product_subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    product_shortdesc= models.CharField(max_length=250)
    product_longdesc= models.TextField()
    product_mrp = models.FloatField(default=1.00)
    product_taxrate = models.PositiveIntegerField(default=18)
    product_weight = models.PositiveBigIntegerField(default=500)
    product_piece = models.PositiveIntegerField(default=1)
    product_stock = models.PositiveIntegerField(default=0)
    product_isactive = models.BooleanField(default=False)
    product_img1 = models.ImageField(upload_to="product", null=True, blank=True)
    product_img2 = models.ImageField(upload_to="product", null=True, blank=True)
    product_img3 = models.ImageField(upload_to="product", null=True, blank=True)
    product_img4 = models.ImageField(upload_to="product", null=True, blank=True)


    created_at =models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_sku +" - "+self.product_name