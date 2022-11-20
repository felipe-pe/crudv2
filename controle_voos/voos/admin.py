from django.contrib import admin
from .models import aeroporto, companhia, voo, orq

# Register your models here.
admin.site.register(companhia)
admin.site.register(voo)
admin.site.register(aeroporto)
admin.site.register(orq)