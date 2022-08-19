from django.contrib import admin

from .models import NoteLenovo

# Register your models here.


class NotebookLenovo(admin.ModelAdmin):
    list_display = ("id" ,"name", "price")
    list_display_links = ("id" ,"name")
    search_fields = ('nome', )

admin.site.register(NoteLenovo, NotebookLenovo)