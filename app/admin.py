from django.contrib import admin

from .models import Post, Categoria, Cargo

admin.site.register(Categoria)

admin.site.register(Cargo)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria','autor','criado')



