from django.contrib import admin
from .models import Film  # Импортируем модель Film из models.py

# Регистрируем модель Film в админ-панели
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'review')  # Отображаемые поля
    search_fields = ('title', 'description')  # Поля для поиска

admin.site.register(Film, FilmAdmin)
