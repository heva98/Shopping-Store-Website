from django.contrib import admin
from .models import FeatureProduct
from .models import LatestProduct

# Register your models here.

admin.site.register(FeatureProduct),
admin.site.register(LatestProduct)