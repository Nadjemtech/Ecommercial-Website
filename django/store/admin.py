from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

admin.site.register(Category , MPTTModelAdmin)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductSpecification)
admin.site.register(ProductSpecificationValue)
admin.site.register(ProductImage)

# Register your models here.
