from django.contrib import admin
from .models import Usuario, Genero, Idioma, Autor, Livro, Emprestimo
# Register your models here.

# lista de tabelas 
admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Emprestimo)

