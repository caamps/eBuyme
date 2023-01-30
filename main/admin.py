from django.contrib import admin
from .models import User, Estado, Anuncio, CategoriaProd, Imagens

admin.site.register(Estado)
admin.site.register(User)
admin.site.register(Anuncio)
admin.site.register(CategoriaProd)
admin.site.register(Imagens)
# Register your models here.
