from django.contrib import admin
# add Feeding to the import
from .models import Widget

admin.site.register(Widget)
