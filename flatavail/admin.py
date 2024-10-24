from django.contrib import admin
from flatavail.models import category_db,product_db

# Register your models here.
admin.site.register(category_db)
admin.site.register(product_db)
