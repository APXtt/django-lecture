from django.contrib import admin
from .models import parentModel as pM, childModel as cM

# Register your models here.
admin.site.register(pM)
admin.site.register(cM)
