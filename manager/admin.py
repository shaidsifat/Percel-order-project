from django.contrib import admin

# Register your models here.

from .models import createnewpercel
from .models import createorder,createcheckorder
# Register your models here.
admin.site.register(createnewpercel)
admin.site.register(createorder)
admin.site.register(createcheckorder)