from django.contrib import admin
from .models import Categoría, Producto
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado_en', 'stock', 'puntaje')


admin.site.register(Categoría, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
