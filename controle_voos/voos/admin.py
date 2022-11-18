from django.contrib import admin
from .models import companhia, Voo, partida, chegada

# Register your models here.
admin.site.register(companhia)
admin.site.register(Voo)
admin.site.register(partida)
admin.site.register(chegada)