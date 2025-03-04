from django.contrib import admin
from .models import Textbook

@admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'course_code', 'edition', 'condition', 'availability')
    list_filter = ('course_code', 'availability')
    search_fields = ('title', 'author', 'course_code')

