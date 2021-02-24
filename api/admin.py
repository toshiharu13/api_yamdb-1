from django.contrib import admin
from .models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Genre, GenreAdmin)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description',)


admin.site.register(Title, TitleAdmin)