from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey




class Category(MPTTModel):
    name = models.CharField(max_length=255 , verbose_name = _("Category Name"),help_text = _("Required and unique"),unique=True)
    slug = models.SlugField(verbose_name =_("Category save URL"), max_length = 255 , unique=True )
    parent = TreeForeignKey("self" , on_delete = models.CASCADE , null = True ,blank = True , related_name = "children")
    is_active = models.BooleanField(default = True)


    class MPTTMeta :
        order_insertion_by = ["name"]
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    def get_absolute_url(self):
        return reverse('store:category_list', args = [self.slug])
    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255 , verbose_name="Product Name", help_text="Required")
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductType'
        verbose_name_plural = 'ProductTypes'    


class ProductSpecification(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255 , verbose_name="Name", help_text="Required")
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductSpecification'
        verbose_name_plural = 'ProductSpecifications'



class Product(models.Model):
    product_type = models.ForeignKey(ProductType , on_delete=models.RESTRICT)
    category = models.ForeignKey( Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255 , verbose_name = _("title"),help_text = _("Required"),unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        error_messages =  {
            "name":{
                "max_length":_("the price between 0 - 999.99"),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        error_messages =  {
            "name":{
                "max_length":_("the price between 0 - 999.99"),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add = True , editable = False)
    updated_at = models.DateTimeField(_("Created at"), auto_now = True)
    def get_absolute_url(self):
        return reverse('store:product_detial', args = [self.slug])
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'            

class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specificatoin = models.ForeignKey(ProductSpecification, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.product

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductSpecificationValue'
        verbose_name_plural = 'ProductSpecificationValues'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "images/",default = "images/default.png",)
    alt_text = models.CharField(max_length=255,blank=True, null=True)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add = True , editable = False)
    updated_at = models.DateTimeField(_("Created at"), auto_now = True)
    def __str__(self):
        self.product

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'