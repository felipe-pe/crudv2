from django.contrib import admin
from .models import companhia, voo, partida, chegada

# Register your models here.
admin.site.register(companhia)
admin.site.register(voo)
admin.site.register(partida)
admin.site.register(chegada)